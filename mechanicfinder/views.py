from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from .forms import ClientRegistrationForm,GarageRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Business
# Create your views here.
def home(request):
    return render(request,"home.html")
    

def landingpage(request):
    businesses = Business.objects.filter(user=request.user)
    return render(request,"landingpage.html",{"businesses":businesses})
   
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
        return redirect('login')

class garage_register(CreateView):
    model = User
    form_class = GarageRegistrationForm
    template_name='garage_register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('login')      

def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('landingpage')
            else:
                messages.error(request,"Invalid username or password") 
        else:
                messages.error(request,"Invalid username or password")       
    return render(request,'login.html',{'form':AuthenticationForm})        

def logout_request(request):
    logout(request)
    return redirect('login')