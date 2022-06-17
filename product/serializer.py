from rest_framework import serializers
from .models import Product,TYPE_CHOICES_2

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name','catagory','description', 'price', 'img','availability']