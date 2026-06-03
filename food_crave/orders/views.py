from django.shortcuts import render, redirect
from .models import Cart, cart_items
from restaurants.models import food_items


def cart(request):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        cart = Cart.objects.get(customer=request.user)
        items = cart.cart_items_set.all()   
    except Cart.DoesNotExist:
        cart = None
        items = []

    total = sum(item.quantity * item.food_item.price for item in items)

    return render(request, 'orders/cart.html', {'items': items,'total': total})



def checkout(request):

    if not request.user.is_authenticated:
        return redirect('login')

def checkout(request):

    if not request.user.is_authenticated:
        return redirect('login')
  
    try:
        cart = Cart.objects.get(customer=request.user)
        items = cart.cart_items_set.all()
    except Cart.DoesNotExist:
        cart = None
        items = []

    total = 0

    for item in items:
        item.subtotal = item.quantity * item.food_item.price
        total += item.subtotal

    return render(request, 'orders/checkout.html', {'items': items,'total': total})


def order_history(request):
    return render(request, 'orders/order_history.html')


def add_to_cart(request):

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        try:
            food_id = request.POST.get('food_id')
            quantity = int(request.POST.get('quantity', 1))

            food = food_items.objects.get(id=food_id)

            cart, created = Cart.objects.get_or_create(
                customer=request.user
            )

            try:
                item = cart_items.objects.get(cart=cart, food_item=food)
                item.quantity += quantity
                item.save()

            except cart_items.DoesNotExist:
                cart_items.objects.create(
                    cart=cart,
                    food_item=food,
                    quantity=quantity
                )

        except food_items.DoesNotExist:
            return redirect('home')

        return redirect('cart')

    return redirect('home')


def remove_from_cart(request, item_id):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        cart = Cart.objects.get(customer=request.user)
        item = cart_items.objects.get(id=item_id, cart=cart)
        item.delete()

    except (Cart.DoesNotExist, cart_items.DoesNotExist):
        pass

    return redirect('cart')