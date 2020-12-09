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
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=20)
    phone_number = models.IntegerField(default=0,null=False)
    cert = models.ImageField(upload_to="images",default="cert.jpg")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.business_name

    @classmethod
    def search_location(cls, name):
        return cls.objects.filter(location__icontains=name).all()

    def delete_business(self):
        return self.delete()

class Feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    business = models.ForeignKey(Business,on_delete=models.CASCADE,default='')
    feedback = models.CharField(max_length=250)
    datecreated= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username