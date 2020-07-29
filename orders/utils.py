from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.db.models import Sum
from django.shortcuts import redirect


def send_mail(order):
    subject = 'Your Order Details'
    message = render_to_string('orders/order_details_to_email.html', {
        'user': order.user,
        'date': order.ordered_at,
        'order_id': order.pk,
        'address': order.address,
        'items': order.items.all(),
        'total_price': order.items.aggregate(
            Sum('price')).get('price__sum')
    })
    order.user.email_user(subject, message)
