from django.shortcuts import render
from . forms import register_user,login as lg 
# Create your views here.
def home(request): 

    return render(request,'home.html')
def profile(request):
    return render(request,'accounts/profile.html')
    return render(request,'accounts/profile.html')

def register(request):
    form=register_user()
    if request.POST:
        pass
    return render(request,'accounts/register.html',{'form':form})

def login(request):
    form=lg()
    return render(request,'accounts/login.html',{'form':form})
