from django.shortcuts import render, get_object_or_404, reverse
from .models import Category, Products, ProductImages, Devise, Order, OrderItem, ShippingAdress, Wishlist

# Create your views here.


# Shop's home page
def home(request):
    category = Category.objects.all().order_by('name')
    products = Products.objects.all().filter(available=True)
    context = {
        'categories': category,
        'products' : products
    }
    return render(request, 'shop/home.html', context)


# Product detail and related product 
def shop_detail(request, slug):
    productDetail = get_object_or_404(Products, slug=slug)
    images = ProductImages.objects.filter(products=productDetail)[:8]
    related = Products.objects.filter(category=productDetail.category)[:8]

    context = {
        'details': productDetail,
        'images': images,
        'related': related
    }
    return render(request, 'shop/shop_detail.html', context)



# User Wishlist
def wishlist(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        customer, product = Wishlist.objects.get_or_create(customer=customer, wishlist=product)
        #items 
    context = {
        
    }
    return render(request, 'shop/wishlist.html', context)



# Fonction to add product in the shooping cart
# Shooping Cart
def shoopingCart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =  []
        order = {'get_cart_total': 0}
    context = {
        'items': items,
        'order': order
    }
    return render(request, 'shop/shooping-cart.html', context)


# Checkout page
def checkout(request):
    pass