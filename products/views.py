from django.shortcuts import render, get_object_or_404
from .models import Product
from django.utils import timezone

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request,
                  'products/products-list.html', {'products': products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,
                  'products/product-details.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']

        new_product = Product.objects.create(
            brand=brand, title=title, description=description, price=price)
        return render(request, 'products/product-add-successful.html')

    else:
        return render(request, 'products/product-add.html')


def show_time(request):
    now = timezone.now()
    return render(request, 'show-time.html', {'DATETIME': now})
