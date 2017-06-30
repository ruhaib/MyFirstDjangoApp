from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_id = models.CharField(max_length=50, primary_key=True)
    source_url = models.CharField(max_length=500)
    category = models.CharField(max_length=100, null=True)


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=500)


class Skus(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    price = models.IntegerField()
    availability = models.BooleanField()
