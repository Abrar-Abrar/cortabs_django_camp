from django.shortcuts import render, get_object_or_404
from .models import Product
from django.utils import timezone

# Create your views here.


def home(request):
    return render(request, 'home.html')


def products_list(request):
    products = Product.objects.all()
    return render(request,
                  'products/products-list.html', {'products': products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,
                  'products/product-details.html', {'product': product})


def show_time(request):
    now = timezone.now()
    return render(request, 'show-time.html', {'DATETIME': now})
