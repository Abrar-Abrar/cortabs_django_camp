from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250, blank=True,  null=True)
    price = models.IntegerField(blank=True,  null=True)
    create_at = models.DateField(blank=True,  null=True)

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
