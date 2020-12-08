from django.contrib.auth.forms import UserCreationForm
from .models import User,Client,Garage
from django.db import transaction

class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=false)
        user.is_client = True
        user.save()
        return user



class GarageRegistrationForm(UserCreationForm):
    class Meta:
        model = Garage
        fields =  ['username','email','logo','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=false)
        user.is_mechanic = True
        user.save()
        return user  