from django.urls import path
from .views import order_new

urlpatterns = [
    path('orders/new/', order_new, name='order_new'),
]
