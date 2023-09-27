from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from random import sample


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product(request, product_slug):
    all_products = list(Product.objects.exclude(slug=product_slug).order_by('?')[:4])
    try:
        product = get_object_or_404(Product, slug=product_slug)
    except Product.DoesNotExist:
        product = None
    return render(request, 'product.html', {'product': product, 'featured_products': all_products})
