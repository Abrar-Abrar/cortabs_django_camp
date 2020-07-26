from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product

# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name='carts', on_delete=models.CASCADE)
    item = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_carts(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
