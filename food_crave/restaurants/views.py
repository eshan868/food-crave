from django.shortcuts import render
from .forms import food_items_form
# Create your views here.
def restaurant_dashboard(request):

    return render(request,'restaurants/restaurant_dashboard.html')

def add_food(request):
    form = food_items_form()
    return render(request,'restaurants/add_food.html',{'form': form})
  