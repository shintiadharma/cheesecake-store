from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')

def show_main(request):
    menu_item = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'kelas': 'PBP F',
        'items': [
            {'name': 'Strawberry Cheesecake', 'size': '30x20', 'price': 'RP647.900', 'description': 'A party special that is loved by all. Vanilla flavored baked cheesecake with freshly picked strawberries.', 'notes': 'Customizable for your loved ones special occasion!'},
            {'name': 'Blueberry Cheesecake', 'size': '30x20', 'price': 'RP616.000', 'description': 'Our famous cheesecake pairs perfectly with natural blueberries.', 'notes': 'Customizable for your loved ones special occasion!'},
        ],
        'menu_item': menu_item,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'main.html', context)

def add_menu_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        new_item = form.save(commit=False)
        new_item.user = request.user
        new_item.size = "30x20"  
        new_item.price = 500000 
        new_item.description = "Default description"  
        new_item.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_menu_item.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response