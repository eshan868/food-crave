from django.shortcuts import render

# Create your views here.
def restaurant_dashboard(request):

    return render(request,'restaurants/restaurant_dashboard.html')

def add_food(request):
    
    return render(request,'restaurants/add_food.html')
