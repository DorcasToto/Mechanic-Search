from django.contrib import admin
from .models import Business,User,Client,Garage,Feedback


# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Garage)
admin.site.register(Business)
admin.site.register(Feedback)