from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Cart
from products.models import Product


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)

    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()
    total_price = user.cart.total_price()

    return render(request, 'carts/cart.html', {'products': products,
                                               'total_price': total_price})


@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.get(user=request.user)
    cart.items.remove(product)

    return redirect('cart')


@login_required
def clear_cart(request):
    request.user.cart.items.clear()
    return redirect('cart')
