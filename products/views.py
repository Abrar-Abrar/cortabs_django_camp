from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import AddProductForm
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
        '''
        brand = request.POST['brand']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']

        new_product = Product.objects.create(
            brand=brand, title=title, description=description, price=price)
        '''
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Product added successfully!'
            return render(request, 'products/product-crud-msg.html',
                          {'message': msg})

    else:
        form = AddProductForm()
    return render(request, 'products/product-add.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            msg = 'Product modified successfully!'
            return render(request, 'products/product-crud-msg.html',
                          {'message': msg})

    else:
        form = AddProductForm(instance=product)
    return render(request, 'products/product-add.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.delete():
        msg = 'Product deleted successfully!'
    else:
        msg = 'Product failed to delete!'
    return render(request, 'products/product-crud-msg.html',
                  {'message': msg})


def show_time(request):
    now = timezone.now()
    return render(request, 'show-time.html', {'DATETIME': now})
