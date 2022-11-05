from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html', context={})

def about(request):
    return render(request, 'pages/a-propos.html', context={})


def contact(request):
    return render(request, 'pages/contact.html')