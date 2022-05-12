from django.contrib import admin
from numpy import product
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_Display = ['id','user','name', 'locality', 'city'
    , 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_Display = ['id', 'title', 'selling_price', 
    'discounted_price', 'description', 'brand', 'category'
    , 'product_image' ]


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_Display = ['id', 'user', 'product', 
    'quantity' ]


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_Display = ['id', 'user', 'customer', 'product',
    'quantity', 'ordered_date', 'status'
    ]