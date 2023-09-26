from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('product/<str:product_slug>', views.product, name="Product")
]
