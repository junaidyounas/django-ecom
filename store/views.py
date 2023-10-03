from django.shortcuts import render
from .models import Product,Category,Order
from django.shortcuts import get_object_or_404
from random import sample

from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy


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


def order(request, product_slug):
    try:
        product = get_object_or_404(Product, slug=product_slug)
    except Product.DoesNotExist:
        product = None
    return render(request, 'order.html', {'product': product})

def save_order(request, product_slug):
    # Assuming you have logic to retrieve the product based on the product_slug
    product = get_object_or_404(Product, slug=product_slug)
    print(request)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Order instance and populate it with form data
            order = Order(
                product=product,
                customer=request.user.customer,  # Assuming you have user authentication
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            # Save the order to the database
            order.save()
            print(email)
            # Redirect to a success page
            return redirect('success_page')
    else:
        form = ContactForm()

    return render(request, 'order.html', {'form': form, 'product': product})

