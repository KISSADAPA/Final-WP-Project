from django.contrib import admin

# Register your models here.

from Manage.models import  Product, Promo

admin.site.register(Product)

admin.site.register(Promo)