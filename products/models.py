
from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL


# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to ='uploads/image')
    name = models.CharField(max_length=255,null= False, blank= False)
    price = models.DecimalField(max_digits=6, decimal_places=2,null= False, blank= False)
    description =models.TextField()
    category = models.CharField(max_length=255,null= True, blank= True)
    def __str__(self):
        return self.name

   