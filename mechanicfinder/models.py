from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_mechanic = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone_number = models.IntegerField(default=0,null=False)

class Garage(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    business_name = models.CharField(max_length=20)
    mechanic_name = models.CharField(max_length=20)
    services = models.CharField(max_length=20)
    available = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    cert = models.ImageField(upload_to="images",default="cert.jpg")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.business_name

