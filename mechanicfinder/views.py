from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ClientRegistrationForm,GarageRegistrationForm,BusinessRegistration,FeedbackForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Business,Feedback
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    return render(request,"home.html")
    

def landingpage(request):
    businesses = Business.objects.filter(user=request.user)
    all_businesses = Business.objects.filter(is_approved=True)
    not_approved = Business.objects.filter(user = request.user).filter(is_approved=False)
    approved = Business.objects.filter(user = request.user).filter(is_approved=True)
    params = {
        "businesses":businesses,
        "all_businesses":all_businesses,
        "not_approved":not_approved,
        "approved":approved,
    }
    return render(request,"landingpage.html",params)
   
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

@login_required
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessRegistration(request.POST,request.FILES)
        if form.is_valid():
            formBus = form.save(commit=False)
            formBus.user = current_user
            formBus.save()
            return redirect('landingpage')

    else:
        form = BusinessRegistration()

    return render(request,"new_business.html",{"form":form})

def search_location(request):
    if 'search_business' in request.GET and request.GET['search_business']:
        name = request.GET.get("search_business")
        searchResults = Business.search_location(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any Location"
    return render(request, 'search.html', {'message': message})

def profile(request):
    return render(request,'profile.html')

def delete(request,id):
    business = Business.objects.get(id = id)
    business.delete()
    message = "The record has been deleted successfully"
    return redirect('landingpage')

def update(request,id):
    if request.POST:
        business_form = BusinessRegistration(request.POST)

        if business_form.is_valid():


            bus = Business.objects.get(id=id)
            bus_form = BusinessRegistration(request.POST, instance = bus)
            bus_form.save() 
            return redirect('landingpage')
    else:
        bus = Business.objects.get(pk = id)       
        bus_form = BusinessRegistration(instance=bus)
        params = {
            'form':bus_form,
            'bus':bus,
        }

    return render(request,'edit_business.html',params)

def client_feedback(request,id):
    feed = Business.objects.get(id=id)
    current_user = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            formFeed = form.save(commit=False)
            formFeed.user = current_user
            formFeed.business = feed
            formFeed.save()
            messages.success(request,"Your Feedback has been Sent!")
            return redirect('landingpage')

    else:
        form = FeedbackForm()
        feed = Business.objects.get(id=id)

    return render(request,"client_feedback.html",{"form":form,"feed":feed})

def garage_feedback(request,id):
    # try:    
    #     feedback = Feedback.objects.get(business=id)
    # except ObjectDoesNotExist:
    #     raise Http404("No MyModel matches the given query.")
    # return render(request,'garage_feedback.html',{'feedback':feedback})
    # feedback = get_object_or_404(Feedback,business=id)
    feedback = Feedback.objects.filter(business=id)
    return render(request,'garage_feedback.html',{'feedback':feedback})

def view_business(request,id):
    view_business = Business.objects.get(id = id)
    return render(request,"landingpage.html",{"view_business":view_business})