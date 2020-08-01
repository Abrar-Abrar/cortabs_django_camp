from django.urls import path
from .views import show_time, products_list, product_details,\
    product_add, product_edit, product_delete

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/new/', product_add, name='product_add'),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('products/edit/<int:pk>/', product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
    path('show-time/', show_time)
]
