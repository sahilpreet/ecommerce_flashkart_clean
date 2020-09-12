"""flashkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import index_page_ecomm,category_view,sub_category_view,product_view,cart_view,register_view,login_view,logout_view,customer_view,cart_add_ajax,cart_remove_ajax,search_view,contactus_view,about_view

app_name='ecommerce' 
urlpatterns = [
    #used to generate sitemap
    #path('sitemap.xml', sitemap,{'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},name='django.contrib.sitemaps.views.sitemap'),
    
    path('',index_page_ecomm,name='appindex'),
    path('category/<str:category>',category_view,name='category'),
    path('sub_category/<str:sub_category>',sub_category_view,name='sub_category'),
    path('product_view/<int:id>',product_view,name='product_view'),
    path('cart',cart_view,name='cart'),
    path('cart_add_ajax',cart_add_ajax,name='cart_add_ajax'),
    path('cart_remove_ajax',cart_remove_ajax,name='cart_remove_ajax'),
    path('search_view',search_view,name='search_view'),
    path('contactus',contactus_view,name='contactus'),
    path('about',about_view,name='about'),
    
    path('register',register_view,name='register'),
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('customer',customer_view,name='customer'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


