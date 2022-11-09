from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    
class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    Additionnal = models.TextField(blank=True)
    previews = models.TextField(blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='image', blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} - {self.category}'


    
class ProductImages(models.Model):
    products = models.ForeignKey(Products, related_name='image', default=None,  on_delete=models.CASCADE)
    images = models.FileField(upload_to='images')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

        def __str__(self):
            return self.image.name
        

class Devise(models.Model):
    DEVIDE = (
        ('CFA', 'Francs CFA'),
        ('USD', 'Dollars'),
        ('EUR', 'Euros')
    )
    name = models.CharField(max_length=3, choices=DEVIDE, default='CFA')

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Device'

    def __str__(self):
        return self.name
    