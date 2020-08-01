from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from products.models import Product
from .utils import send_mail

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name="orders", null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    ordered_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=Order)
def fill_address_if_null(sender, instance, **kwargs):
    if not instance.address:
        instance.address = instance.user.user_profile.address


@receiver(post_save, sender=Order)
def after_send_order(sender, instance, **kwargs):
    instance.items.set(instance.user.cart.items.all())
    send_mail(instance)
    instance.user.cart.items.clear()
