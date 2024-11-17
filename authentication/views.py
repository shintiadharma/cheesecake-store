from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .models import Product

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=400)
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

@csrf_exempt
def get_products(request):
    products = Product.objects.all()

    if not products:
        return JsonResponse({
            "status": "success",
            "message": "Tidak ada produk yang tersedia",
            "products": []
        })

    data = [
        {
            "model": "product",
            "pk": str(p.id),
            "fields": {
                "user": p.user.id if p.user else 0,
                "name": p.name,
                "size": p.size,
                "price": float(p.price),
                "description": p.description,
                "notes": p.notes
            }
        }
        for p in products
    ]

    return JsonResponse(data, safe=False)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            print("Menerima request POST dari Flutter")
            print("Headers:", request.headers)
            print("Body:", request.body)

            data = json.loads(request.body)
            name = data.get('name')
            size = data.get('size')
            price = data.get('price')
            description = data.get('description')
            notes = data.get('notes')

            # Cek apakah semua data ada
            if not all([name, size, price, description, notes]):
                return JsonResponse({'status': 'error', 'message': 'Data tidak lengkap'}, status=400)

            print(f"Produk yang diterima: {name}, {size}, {price}, {description}, {notes}")
            return JsonResponse({'status': 'success'}, status=200)

        except Exception as e:
            print("Error:", e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)