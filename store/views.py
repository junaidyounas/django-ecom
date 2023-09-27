from django.shortcuts import render
from .models import Product,Category
from django.shortcuts import get_object_or_404
from random import sample


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all() 

    return render(request, 'home.html', {'products': products, 'categories': categories})

def product(request, product_slug):
    all_products = list(Product.objects.exclude(slug=product_slug).order_by('?')[:4])
    try:
        product = get_object_or_404(Product, slug=product_slug)
    except Product.DoesNotExist:
        product = None
    return render(request, 'product.html', {'product': product, 'featured_products': all_products})

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})

