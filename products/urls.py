from django.urls import path
from . views import *
from . import views

urlpatterns = [
 path('product', ProductView.as_view(), name="product"),]