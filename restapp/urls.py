from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('menu',views.menu,name='menu'),
    path('gallery',views.gallery,name='gallery'),
    path('cart',views.cart,name='cart'),
     path('menus',views.menus,name='menus'),
]