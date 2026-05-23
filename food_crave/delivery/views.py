from django.shortcuts import render

# Create your views here.
def delivery_dashboard(request):
    
    return render(request,'delivery/delivery_dashboard.html')

def new_orders(request):

    return render(request,'delivery/new_orders.html')

def food_display(request):

    return render(request,'food_items/food_display.html')

def food_detail(request):

    return render(request,'food_items/food_detail.html')



