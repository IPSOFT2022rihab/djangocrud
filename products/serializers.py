from dataclasses import fields
from .models import *
from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
         model =  Product
         fields = '__all__'