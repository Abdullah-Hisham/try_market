from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class seller(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    gmail = models.EmailField(max_length=254)
    password= models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    def __str__(self) -> str:
        return (self.first_name+' '+self.last_name)

class product(models.Model):
    seller_name = models.ForeignKey(seller, on_delete=models.CASCADE)
    dis = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    time_pup = models.DateTimeField(auto_now_add=True)

class order(models.Model):
    name = models.CharField( max_length=50)
    quantity = models.PositiveIntegerField()
    adress = models.CharField(max_length=50) 
    phone_num = models.IntegerField()
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)

class reviews(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    review = models.TextField()
    stars = models.IntegerField()