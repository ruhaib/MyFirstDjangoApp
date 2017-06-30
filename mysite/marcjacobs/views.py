from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Images, Skus
import pandas


def display_data(request):
    return render(request, 'base.html', {})


def load_scrappy_data(request):
    scrapped_data = pandas.read_json(
        '/home/ruhaib/py3Scrapy/tutorial/marcjacobs.json')

    for index, row in scrapped_data.iterrows():
        prod = Product()
        prod.product_id = row['product_id']
        prod.product_name = row['product_name']
        prod.category = row['product_category']
        prod.source_url = row['source_url']
        prod.save()
        for img in row['images']:
            images = Images()
            images.product = prod
            images.image_url = img

            images.save()
        for sku in row['skus']:
            prod_sku = Skus()
            prod_sku.product = prod
            prod_sku.color = sku['color']
            prod_sku.availability = sku['availability']
            prod_sku.price = sku['price']
            prod_sku.size = sku['size']
    return HttpResponse('<h1 style="text-align:center"> data loaded ... </h1>')
