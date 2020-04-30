from django import forms
from django.forms.widgets import Textarea


class add_product(forms.Form):
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

    product_name = forms.CharField(max_length=255, label='ชื่อสินค้า')
    producer_name = forms.CharField(max_length=255 , label='ชื่อผู้ผลิต')
    years = forms.CharField(max_length=4 , label='ปีที่ผลิต')
    data = forms.CharField(widget=forms.Textarea , label='ข้อมูลสินค้า')
    category = forms.ChoiceField(choices=CATEGORY_PRODUCT , label='หมวดสินค้า')
    type = forms.ChoiceField(choices=TYPE , label='ชนิดสินค้า')
    status = forms.ChoiceField(choices=STATUS , label='สถานะ')
    price = forms.FloatField(label='ราคา')
    pic_url = forms.ImageField(label='รูป')
    create_time = forms.DateField()
    update_time = forms.DateField()