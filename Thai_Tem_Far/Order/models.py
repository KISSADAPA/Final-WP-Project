from django.db import models
from django.contrib.auth.models import User

from Account.models import Staff, Customer
from Manage.models import Product

# Create your models here.

#----- คำสั่งซื้อ -----
class Order(models.Model):
    order_amount = models.IntegerField()
    order_date = models.DateField(auto_now=True, null=False)
    total_price = models.FloatField()
    sta_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    cus_id = models.ForeignKey(Customer, on_delete=models.PROTECT)

#----- รายละเอียดคำสั่งซื้อ -----
class Order_list(models.Model):
    unit = models.IntegerField()
    unit_price = models.FloatField()
    item_price = models.FloatField()
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)

#----- ใบเสร็จ -----
class Bill(models.Model):
    bill_date = models.DateField(auto_now=True)
    tex_id = models.CharField(max_length=255)
    total_price = models.FloatField()
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)