from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#----- ข้อมูลผู้ผลิต -----
class Producer(models.Model):
    producer_id = models.CharField(max_length=255, primary_key=True, null=False, unique=True)
    producer_name = models.CharField(max_length=255)
    producer_address = models.TextField()
    producer_phone = models.CharField(max_length=10)

#----- ข้อมูลคลังสินค้า -----
class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True, null=False, unique=True)
    stock_number = models.IntegerField()
    order_amount = models.IntegerField()
    location = models.TextField()
    
#----- ข้อมูลสินค้า -----
class Product(models.Model):
    product_id = models.CharField(max_length=255, primary_key=True, null=False, unique=True)
    product_name = models.IntegerField()
    price = models.FloatField()
    picture = models.ImageField(upload_to='images/')
    producer_id = models.ForeignKey(Producer, on_delete=models.PROTECT)
    stock_id = models.ForeignKey(Stock, on_delete=models.PROTECT)