from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Images, Skus
import pandas


def display_data(request):
    products = Product.objects.all()
    return render(request, 'marcjacobsapp/index.html', {'products': products})


def load_scrappy_data(request):
    scrapped_data = pandas.read_json(
        '/home/ruhaib/py3Scrapy/tutorial/marcjacobs.json')

    # products = []
    # images_list = []
    # skus_list = []
    for index, row in scrapped_data.iterrows():
        prod = Product()
        prod.product_id = row['product_id']
        prod.product_name = row['product_name']
        prod.category = row['product_category']
        prod.source_url = row['source_url']
        prod.save()
        # products.add(prod)
        for img in row['images']:
            images = Images()
            images.product = prod
            images.image_url = img

            images.save()
            # images_list.append(images)
        for sku in row['skus']:
            prod_sku = Skus()
            prod_sku.product = prod
            prod_sku.color = sku['color']
            prod_sku.availability = sku['availability']
            prod_sku.price = sku['price']
            prod_sku.size = sku['size']
            prod_sku.save()
            # skus_list.append(prod_sku)

    # Product.objects.bulk_create(products)
    # Images.objects.bulk_create(images_list)
    # Skus.objects.bulk_create(skus_list)
    return HttpResponse('<h1 style="text-align:center"> data loaded ... </h1>')
