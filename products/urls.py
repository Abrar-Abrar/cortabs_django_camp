from django.urls import path
from .views import show_time, products_list, product_details, product_add

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/add', product_add, name='product_add'),
    path('products/<pk>', product_details, name='product_details'),
    path('show-time/', show_time)
]
