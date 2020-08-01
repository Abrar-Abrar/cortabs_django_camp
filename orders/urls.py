from django.urls import path
from .views import order_new, orders_list

urlpatterns = [
    path('orders/', orders_list, name='order_list'),
    path('orders/new/', order_new, name='order_new'),
]
