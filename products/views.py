from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic import TemplateView
from rest_framework import status
from django.db import connection
# Create your views here.
class ProductView(generics.ListAPIView):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer



