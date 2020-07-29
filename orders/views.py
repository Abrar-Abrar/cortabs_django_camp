from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CheckoutForm

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
