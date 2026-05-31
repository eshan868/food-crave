from django.shortcuts import render,redirect
from . forms import register_user,Login  
from django.contrib.auth import authenticate ,login as authlogin
# Create your views here.
def home(request): 

    return render(request,'home.html')
def profile(request):
 
    return render(request,'accounts/profile.html')

def register(request):
   
    if request.POST:
        form=register_user(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(
            form.cleaned_data['password']
)

            form.save()
            print("User Saved Successfully")
            return redirect('login')
    else:
        form=register_user()

    return render(request,'accounts/register.html',{'form':form})


def customer_dashboard(request):

    return render(request,'user/user-dashboard')