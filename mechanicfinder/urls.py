from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.login_request,name = 'home'),
    path('landingpage/',views.landingpage,name = 'landingpage'),
    path('garage_home/',views.garage_home,name = 'garage_home'),
    path('client_register/',views.client_register.as_view(),name = 'client_register'),
    path('garage_register/',views.garage_register.as_view(),name = 'garage_register'),
    path('new_business/',views.new_business,name = 'new_business'),
    path('search/',views.search_location,name = 'search_location'),
    path('profile/',views.profile,name = 'profile'),
    path('login/',views.login_request,name = 'login'),
    path('logout/',views.logout_request,name = 'logout'),

     
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)