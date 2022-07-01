from django.urls import path
from . views import *
from . import views

urlpatterns = [
 path('product/<int:pk>', ProductView.as_view(), name="product"),

 path('product/',  ProductAdd.as_view(), name="product"),
 
 ]