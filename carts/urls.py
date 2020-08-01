from django.urls import path
from .views import add_to_cart, cart, remove_from_cart, clear_cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove_from_cart/<int:pk>/',
         remove_from_cart, name='remove_from_cart'),
    path('cart/clear_cart/', clear_cart,
         name='clear_cart'),
]
