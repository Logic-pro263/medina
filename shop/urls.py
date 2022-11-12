from django.urls import path
from . import views


urlpatterns = [
    path('Boutique/', views.home, name='home'),
    path('detail/<int:product_id>', views.shop_detail, name='detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('shooping-cart', views.shoopingCart, name='shooping-cart'),
    path('payement', views.checkout, name='checkout')
]
