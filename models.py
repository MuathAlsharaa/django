from argparse import _MutuallyExclusiveGroup
from distutils.command.upload import upload
from email.policy import default
from tracemalloc import Trace
from unicodedata import category, digit
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)





X=[
    ('available','available'),
    ('Sold','Sold'),

]


class Book(models.Model):
    title=models.TextField(max_length=250)
    autohr = models.TextField(max_length=20,null=True,blank=True)
    photo_autohr = models.ImageField(upload_to='photos',null=True,blank=True)
    image=models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    
    price = models.IntegerField(max_length=4)
    
    activate = models.BooleanField(default=False)
    # هاذا الخيار المسؤول عن اذا كان الكتاب موجود ام لا
    status =models.CharField(max_length=50,choices=X,default='')
    
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default='')