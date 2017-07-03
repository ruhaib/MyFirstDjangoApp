from django.contrib.postgres.fields import JSONField
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_id = models.CharField(max_length=50, default="")
    source_url = models.URLField()
    category = models.CharField(max_length=100, null=True)


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField()


class Skus(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20, null=True)
    price = models.IntegerField()
    availability = models.BooleanField()


class Menu(models.Model):
    name = models.CharField(max_length=100)
    categories = JSONField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, default="")
