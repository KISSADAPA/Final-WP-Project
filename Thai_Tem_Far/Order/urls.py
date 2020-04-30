from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('cart/', views.cart_page, name='cart'),

    path('<int:id_product>/', views.detail, name = 'detail'),
    path('<int:id_product>/booking/', views.booking, name = 'booking'),

    path('confirm/<int:id_buy>/', views.confirm, name = 'confirm'),
    path('status/', views.reservation_list, name='status'),
    
    path('admin/Manage/product/add/', views.add_edit_product, name='add_edit_product'),
    path('admin/Manage/product/<int:id_product>/change/', views.change_product, name='change_product'),
    path('product_detail/<int:id_product>', views.product_detail, name='product_detail')
]