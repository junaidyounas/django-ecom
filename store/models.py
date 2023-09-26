from django.db import models
import datetime
import django.db.models.deletion
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.full_name}'

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=750, default='', blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True)

    class Meta:
        unique_together = ('name', 'slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product/')

# Signal handler to delete associated image file
@receiver(pre_delete, sender=ProductImages)
def delete_image(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    instance.image.delete(False)  # Passing False to delete the file immediately


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.TextField(max_length=200, default='', blank=True, null=True)
    phone = models.CharField(max_length=12, default='', blank='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

