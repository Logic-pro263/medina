from django.shortcuts import render
from shop.models import Products

# Create your views here.


def index(request):
    products = Products.objects.all().filter(available=True)[:8]
    context ={
        'products': products
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/a-propos.html', context={})


def contact(request):
    return render(request, 'pages/contact.html')