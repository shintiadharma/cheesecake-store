from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    menu_item = Product.objects.all()
    context = {
        'name': 'Shintia Dharma Shanty',
        'kelas': 'PBP F',
        'items': [
            {'name': 'Strawberry Cheesecake', 'size': '30x20', 'price': 'RP647.900', 'description': 'A party special that is loved by all. Vanilla flavored baked cheesecake with freshly picked strawberries.', 'notes': 'Customizable for your loved ones special occasion!'},
            {'name': 'Blueberry Cheesecake', 'size': '30x20', 'price': 'RP616.000', 'description': 'Our famous cheesecake pairs perfectly with natural blueberries.', 'notes': 'Customizable for your loved ones special occasion!'},
        ],
        'menu_item': menu_item
    }
    return render(request, 'main.html', context)

def add_menu_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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