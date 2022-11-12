from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    


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
    digital = models.BooleanField(default=False, null=True, blank=False)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} - {self.category}'

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url=''
        return url


    
class ProductImages(models.Model):
    products = models.ForeignKey(Products, related_name='image', default=None,  on_delete=models.CASCADE)
    images = models.FileField(upload_to='images')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

        def __str__(self):
            return self.image.name
        

class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self): 
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


# Customer' order
class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} - {self.quantity}'

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100)
    about_note = models.BooleanField(default=False)
    order_note = models.TextField()
    date_add =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


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
    

class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = ("Favoris")
        verbose_name_plural = ("Favoris")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Favoris_detail", kwargs={"pk": self.pk})
