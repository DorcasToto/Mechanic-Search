from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import ClientRegistrationForm,GarageRegistrationForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def client_home(request):
    return render(request,"client_home.html")

def garage_home(request):
    return render(request,"garage_home.html")

class client_register(CreateView):
#    if request.method == 'POST':
#        form = ClientRegistrationForm(request.POST)
#         return render('client_register.html',{'form':form})
    # template = 'client_register.html'

    model = User
    form_class = ClientRegistrationForm
    template_name='client_register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('client_home')

class garage_register(CreateView):
    model = User
    form_class = GarageRegistrationForm
    template_name='garage_register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('garage_home')      