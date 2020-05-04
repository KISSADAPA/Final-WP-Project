from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#----- ข้อมูลู้ผลิต -----
class Producer(models.Model):
    producer_name = models.CharField(max_length=255)
    producer_address = models.TextField()
    producer_phone = models.CharField(max_length=10)

#----- ข้อมูลสินค้า -----
class Stock(models.Model):
    stock_number = models.IntegerField()
    order_amount = models.IntegerField()
    location = models.TextField()
    
#----- ข้อมูลสินค้า -----
class Product(models.Model):

    CATEGORY_PRODUCT = (
        ('EL','Electrical Line'),
        ('IL','Insuments Line'),
        ('TL','Tools Line'),
        ('MCL','Material Consumable Line'),
        ('SEL','Safety Equipment Line'),
        ('ILT','Insuments Line-Temperature'),
        ('ILF','Insuments Line-Flow Meter'),
        ('ITP','Insuments Line-Pressure'),
        ('AL','Accessoreis Line'),
        ('CL','Consumable Line')
    )

    TYPE = (
        ('BL','Business Line'),
        ('VI','Vision'),
        ('MI','Mission')
    )

    STATUS = (
        ('AVAILABLE','มีสินค้า'),
        ('NO_AVAILABLE','ไม่มีสินค้า'),
        ('HIDE','ซ่อน')
    )

    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    pic_url = models.ImageField(upload_to='images/')
    producer_id = models.ForeignKey(Producer, on_delete=models.DO_NOTHING)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    years = models.CharField(max_length=4)
    information = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORY_PRODUCT)
    type = models.CharField(max_length=10, choices=TYPE)
    status = models.CharField(max_length=12, choices=STATUS)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

#----- โปรโมชั่น -----
class Promo(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    promotion_code = models.CharField(max_length=8,unique=True)
    discount_percent = models.FloatField()
    minimum_cost = models.FloatField()
    expire_day = models.DateTimeField()
    is_active = models.BooleanField()
    