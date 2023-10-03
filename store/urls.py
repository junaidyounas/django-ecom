from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('product/<str:product_slug>', views.product, name="Product"),
    path('category/<str:category_slug>', views.category_products, name="Category"),
    path('order/<str:product_slug>', views.order, name="Order"),
]
