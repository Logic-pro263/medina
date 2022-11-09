from django.contrib import admin
from .models import Category, Products, Devise, ProductImages
# Register your models here.


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages


admin.site.register(Category)

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


admin.site.register(Devise)