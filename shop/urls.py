from django.urls import path
from . import views


urlpatterns = [
    path('Boutique/', views.home, name='home'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('shooping-cart', views.shoopingCart, name='shooping-cart'),
    path('detail/<int:product_id>', views.shop_detail, name='detail'),
]
