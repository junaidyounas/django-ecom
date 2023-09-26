from django.contrib import admin
from .models import Category, Customer, Product, Order, Order, ProductImages


class ImageInline(admin.TabularInline):  # You can also use StackedInline for a different layout
    model = ProductImages
    extra = 1  # Number of empty forms to display for adding images

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductImages)

# Register your models here.
