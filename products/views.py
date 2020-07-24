from django.shortcuts import render, redirect, get_object_or_404
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
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                msg = 'Product added successfully!'
                return render(request, 'products/product-crud-msg.html',
                              {'message': msg})

        else:
            form = AddProductForm()
        return render(request, 'products/product-add.html', {'form': form})
    else:
        return redirect('products_list')


def product_edit(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = AddProductForm(
                request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                msg = 'Product modified successfully!'
                return render(request, 'products/product-crud-msg.html',
                              {'message': msg})

        else:
            form = AddProductForm(instance=product)
        return render(request, 'products/product-add.html', {'form': form})
    else:
        return redirect('products_list')


def product_delete(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)

        if product.delete():
            msg = 'Product deleted successfully!'
        else:
            msg = 'Product failed to delete!'
        return render(request, 'products/product-crud-msg.html',
                      {'message': msg})
    else:
        return redirect('products_list')


def show_time(request):
    now = timezone.now()
    return render(request, 'show-time.html', {'DATETIME': now})
