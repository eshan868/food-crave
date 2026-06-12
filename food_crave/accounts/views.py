from django.shortcuts import render,redirect
from . forms import register_user,Login,EditProfile
from django.contrib.auth import authenticate ,login as authlogin,logout
# Create your views here.
def home(request): 

    return render(request,'home.html')
def profile(request):
    user =request.user

    return render(request,'accounts/profile.html',{'user_data':user })
def edit_profile(request):

    if request.method == "POST":

        form = EditProfile(

            request.POST,
            request.FILES,
            instance=request.user

        )

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = EditProfile(

            instance=request.user

        )

    return render(request,'accounts/edit_profile.html',{'form': form})

def register(request):
   
    if request.POST:
        form=register_user(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            latitude = request.POST.get("latitude")
            longitude = request.POST.get("longitude")
            user.latitude = latitude
            user.longitude = longitude
            user.set_password(
            form.cleaned_data['password']
            )

            user.save()
            print("User Saved Successfully")
            return redirect('login')
    else:
        form=register_user()

    return render(request,'accounts/register.html',{'form':form})

def login(request):
    form=Login()
    if request.method == 'POST':
        form=Login(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(
                request,
                username=username,
                password=password

            )
            print("Form Valid:", form.is_valid())
            print("Username:", username)
            print("User:", user)

            if user is not None:
                authlogin(request,user)
                if user.role == 'customer':
                    return redirect('customer-dashboard')
                if user.role == 'delivery_man':
                    return redirect('delivery-man-dashboard')
                if user.role == 'restaurant_owner':
                    return redirect('restaurant-owner-dashboard')
                

                
            else:
                
                return render(
                    request,
                    'accounts/login.html',
                    {
                        'form': form,
                        'error': 'Invalid Username or Password'
                    }
                )
      
    return render(request,'accounts/login.html',{'form':form})

def customer_dashboard(request):

    return render(request,'user/user_dashboard.html')


def  user_logout(request):
    logout(request)

    return redirect('login')