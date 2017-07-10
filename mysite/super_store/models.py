from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    brand_link = models.URLField()
    image_icon = models.URLField()

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_id = models.CharField(max_length=50)
    source_url = models.URLField()
    category = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_id+' '+self.product_name


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return self.product.product_id + 'product\'s image'


class Skus(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField()
    availability = models.BooleanField()

    def __str__(self):
        return self.product.product_id + 'product\'s Sku'


class Menu(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=500, default='')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
