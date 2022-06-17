from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# TYPE_CHOICES=[
#     ('phone','PHONE')

# ]
TYPE_CHOICES_2=[
    ('mobile','MOBILE'),
    ('lipstick','LIPStick'),
    ('baal','BAAL')
      
]
class Product(models.Model):
    name= models.CharField(max_length=20, default='')
    catagory= models.CharField(max_length=20,choices=TYPE_CHOICES_2,default='')
    description= models.CharField(max_length=300, default='')
    quantity=models.IntegerField()
    price= models.IntegerField()
    availability= models.BooleanField()
    img= models.ImageField(null=True, blank=True)
    