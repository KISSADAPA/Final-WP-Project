from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#----- ข้อมูลลูกค้า -----
class Customer(models.Model):
    cus_fname = models.CharField(max_length=50, null=False)
    cus_lname = models.CharField(max_length=50, null=False)
    cus_email = models.EmailField(max_length=254, null=False, unique=True)
    cus_phone = models.CharField(max_length=10)
    cus_address = models.TextField()
    account = models.ForeignKey(User, on_delete=models.PROTECT)

#----- ข้อมูลพนักงาน(ทั้งหมด) -----
class Staff(models.Model):    
    sta_fname = models.CharField(max_length=50, null=False)
    sta_lname = models.CharField(max_length=50, null=False)
    sta_email = models.EmailField(max_length=254, null=False, unique=True)
    sta_phone = models.CharField(max_length=10)
    sta_position = models.CharField(max_length=50, null=False)
    account = models.ForeignKey(User, on_delete=models.PROTECT)