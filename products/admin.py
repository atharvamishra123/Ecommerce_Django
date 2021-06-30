from django.contrib import admin

# Register your models here.
from products.models import Products, Sub_Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'pic']


@admin.register(Sub_Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'pic', 'product']


# @admin.register(UserProducts)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['user_reference', 'product_reference']
