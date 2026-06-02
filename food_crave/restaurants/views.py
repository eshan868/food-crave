from django.shortcuts import render,redirect
from .forms import food_items_form,Restaurant_form
from restaurants.models import Restaurant,food_items


# Create your views here.
def restaurant_dashboard(request):

    return render(request,'restaurants/restaurant_dashboard.html')

def add_food(request):

    if request.method == 'POST':

        form = food_items_form(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

    else:
           form = food_items_form()
  

    return render(request,'restaurants/add_food.html',{'form': form})

def add_restaurant(request):

    if request.method == 'POST':

        form = Restaurant_form(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            restaurant = form.save(commit=False)

            restaurant.owner = request.user

            restaurant.save()

            print("Restaurant Created")
            redirect('restaurant-owner-dashboard')

    else:
        form = Restaurant_form()

    return render(
        request,
        'restaurants/add_restaurant.html',
        {'form': form}
    )

def food_display(request):
    food=food_items.objects.all()
 
     
    return render(request,'food_items/food_display.html',{'foods':food})

def food_detail(request):

    return render(request,'food_items/food_detail.html')



