from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('client_home/',views.client_home,name = 'client_home'),
    path('garage_home/',views.garage_home,name = 'garage_home'),
    path('client_register/',views.client_register.as_view(),name = 'client_register'),
    path('garage_register/',views.garage_register.as_view(),name = 'garage_register'),
]