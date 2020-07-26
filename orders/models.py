from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE)
    item = models.ManyToManyField(Product)
    ordered_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
