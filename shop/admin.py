from django.contrib import admin
from .models import Category, Products, Order, Devise, ProductImages, Customer, OrderItem, ShippingAdress
# Register your models here.


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages


admin.site.register(Category)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity', 'date_added']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['name', 'price', 'category']
    list_filter = ['category']

    class Meta:
        model = Products


@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass



admin.site.register(Devise)