from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from  django.conf import settings
from django.conf.urls.static import static
from pages import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
