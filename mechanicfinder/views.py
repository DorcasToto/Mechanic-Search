from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import ClientRegistrationForm,GarageRegistrationForm

# Create your views here.
def register(request):
    return render(request,"register.html")

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
        return redirect('register')