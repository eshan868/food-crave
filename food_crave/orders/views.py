from django.shortcuts import render
# Create your views here.
def cart(request):

    return render(request,'orders/cart.html')
 

def checkout(request):
    
    return render(request,'orders/checkout.html')

def order_history(request):
    
    return render(request,'orders/oder_history.html')
