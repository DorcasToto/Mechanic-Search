from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('client_register/',views.client_register.as_view(),name = 'client')
]