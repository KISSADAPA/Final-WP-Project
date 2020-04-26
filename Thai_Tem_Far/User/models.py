from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#----- ข้อมูลลูกค้า -----
class Customer(models.Model):
    cus_id = models.CharField(max_length=255, primary_key=True, null=False, unique=True)
    cus_fname = models.CharField(max_length=50, null=False)
    cus_lname = models.CharField(max_length=50, null=False)
    cus_email = models.EmailField(max_length=254, null=False)
    cus_phone = models.CharField(max_length=10)
    cus_address = models.TextField()
    username = models.CharField(max_length=150, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)

#----- ข้อมูลพนักงาน(ทั้งหมด) -----
class Staff(models.Model):
    sta_id = models.CharField(max_length=255, primary_key=True, null=False, unique=True)
    sta_fname = models.CharField(max_length=50, null=False)
    sta_lname = models.CharField(max_length=50, null=False)
    sta_posistion = models.CharField(max_length=50, null=False)