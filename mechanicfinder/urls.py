from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_request,name = 'home'),
    path('landingpage/',views.landingpage,name = 'landingpage'),
    path('garage_home/',views.garage_home,name = 'garage_home'),
    path('client_register/',views.client_register.as_view(),name = 'client_register'),
    path('garage_register/',views.garage_register.as_view(),name = 'garage_register'),
    path('login/',views.login_request,name = 'login'),
    path('logout/',views.logout_request,name = 'logout'),
     
]