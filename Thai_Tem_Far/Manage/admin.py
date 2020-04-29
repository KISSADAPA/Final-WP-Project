from django.contrib import admin

# Register your models here.

from Manage.models import Producer, Stock, Product, Promo

admin.site.register(Producer)

admin.site.register(Stock)

admin.site.register(Product)

admin.site.register(Promo)