from django.urls import path
from .views import show_time, home, products_list, product_details

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('show-time/', show_time),
    path('products/<pk>', product_details, name='product_details'),
    path('https://safe-eyrie-78531.herokuapp.com/', home, name='home')
]
