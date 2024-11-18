from django.urls import path
from authentication.views import login, register, data_view, get_products, logout
from main.views import create_product_flutter

app_name = 'authentication'

urlpatterns = [
    path('data/', data_view, name='data'),
    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('products/', get_products, name='get_products'),
    path('auth/logout/', logout, name='logout'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]