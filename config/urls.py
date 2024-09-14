from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', catalog_views.home, name='home'),
    path('contacts/', catalog_views.contacts, name='contacts'),
    path('products/', catalog_views.products, name='products'),
]
