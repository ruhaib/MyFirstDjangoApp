from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    brand_link = models.URLField()
    image_icon = models.URLField()


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_id = models.CharField(max_length=50)
    source_url = models.URLField()
    category = models.CharField(max_length=500, null=True)


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
    category = models.CharField(max_length=500, default='')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
