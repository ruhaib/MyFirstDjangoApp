from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
import ast


def display_data(request):
    products = Product.objects.all()
    return render(request, 'marcjacobsapp/index.html', {'products': products})


class ListProductView(ListView):

    model = Product
    template_name = 'marcjacobsapp/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'marcjacobsapp/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['category'] = ast.literal_eval(context['product'].category)
        context['colors'] = set()
        context['sizes'] = set()
        prod = context['product']
        for color in prod.skus_set.all():
            context['colors'].add(color.color)
            context['sizes'].add(color.size)
        return context
