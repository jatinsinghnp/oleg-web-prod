from django.contrib import admin
from .models import Product, ProductCatageory

# Register your models here.
admin.site.register([Product, ProductCatageory])
