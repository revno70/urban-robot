from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Customer(models.Model):
    c_id=models.IntegerField(primary_key=True)
    full_name=models.CharField(max_length=100) 
    email= models.CharField(max_length=100) 
    phone= models.CharField(max_length=100) 
    userprofile = models.ForeignKey(User, on_delete= models.CASCADE) 

class ProductMenu(models.Model):
    p_id=models.IntegerField(primary_key=True)
    p_name= models.CharField(max_length=100) 
    p_quanity=models.IntegerField() 
    p_price= models.FloatField()
   

