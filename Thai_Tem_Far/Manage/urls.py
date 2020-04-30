from django.urls import path
from django.contrib import admin 
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('buy_approve/<int:id_buy>/', views.buy_approve, name='buy_approve'),
    path('buy_deniel/<int:id_buy>/', views.buy_deniel, name='buy_deniel'),
    path('product', views.product_dashboard, name='product'),
    
    path('product-hidden/<int:id_product>/', views.product_hide, name='product_hide'),
    path('product-unhidden/<int:id_product>/', views.product_unhide, name='product_unhide'),
    path('home-product-hidden/<int:id_product>/', views.home_product_hide, name='home_product_hide'),
    path('available/<int:id_buy>/', views.available, name='available'),
    path('notavailable/<int:id_buy>/', views.notavailable, name='notavailable'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 