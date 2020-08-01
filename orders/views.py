from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CheckoutForm
from .models import Order

# Create your views here.


@login_required
def order_new(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return render(request, 'orders/order_send_to_email_success.html')
    else:
        if not request.user.cart.items.exists():
            return redirect('cart')
        else:
            form = CheckoutForm()
    return render(request, 'orders/order-new.html', {'form': form})


@login_required
def orders_list(request):
    # orders = Order.objects.filter(user=request.user)
    orders = request.user.orders
    return render(request, 'orders/order_list.html', {'orders': orders})
