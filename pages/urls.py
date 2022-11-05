from django.urls import path
from . import views


urlpatterns = [
    path('A Propos', views.about, name='about'),
    path('Contact', views.contact, name='contact'),
]
