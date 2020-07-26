from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True,  null=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateField(default=date.today())
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', null=True)

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
