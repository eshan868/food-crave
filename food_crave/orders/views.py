from django.shortcuts import render, redirect
from .models import Cart, cart_items, Order
from restaurants.models import food_items
from accounts.models import User
from food_crave.utils import calculate_distance
import random
from decimal import Decimal
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        cart = Cart.objects.get(customer=request.user)
        items = cart.cart_items_set.all()

    except Cart.DoesNotExist:
        items = []

    total = sum(
        item.quantity * item.food_item.price
        for item in items
    )

    return render(
        request,
        'orders/cart.html',
        {
            'items': items,
            'total': total
        }
    )

@login_required
def checkout(request):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        cart = Cart.objects.get(customer=request.user)
        items = cart.cart_items_set.all()

    except Cart.DoesNotExist:
        items = []

    total = 0

    for item in items:

        item.subtotal = (
            item.quantity *
            item.food_item.price
        )

        total += item.subtotal  
    delivery_charge = 40
    gst = total * Decimal('0.05')
    grand_total = total + delivery_charge + gst



    return render(
        request,
        'orders/checkout.html',
        {
            'items': items,
            'total': total,
            'delivery_charge': delivery_charge,
            'gst': gst,
            'grand_total': grand_total,
        }
    )



@login_required
def place_order(request):

    if request.method != 'POST':
        return redirect('checkout')

    cart = Cart.objects.get(
        customer=request.user
    )

    items = cart.cart_items_set.all()

    if not items.exists():
        return redirect('cart')

    total = 0

    for item in items:

        total += (
            item.quantity *
            item.food_item.price
        )

    restaurant = (
        items.first()
        .food_item
        .restaurant
    )
    nearest_delivery_man = None
    minimum_distance = float('inf')

    delivery_mans = User.objects.filter(
    role='delivery_man'
    )
       
    for rider in delivery_mans:

        if (
        rider.latitude is None
        or rider.longitude is None
        or restaurant.latitude is None
        or restaurant.longitude is None
        ):
          continue

    distance = calculate_distance(
        restaurant.latitude,
        restaurant.longitude,
        rider.latitude,
        rider.longitude
        )

    if distance < minimum_distance:

        minimum_distance = distance
        nearest_delivery_man = rider

    order = Order.objects.create(
        customer=request.user,
        restaurant=restaurant,
        total_price=total,
        delivery_fee=150,
        status='placed'
    )
    if nearest_delivery_man:

       order.delivery_man = nearest_delivery_man


    order.delivery_otp = str(
        random.randint(
            100000,
            999999
        )
    )

    order.save()

    items.delete()
    return redirect('order_history')

@login_required
def order_history(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/order_history.html',
        {
            'orders': orders
        }
    )

@login_required
def add_to_cart(request):

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        try:

            food_id = request.POST.get(
                'food_id'
            )

            quantity = int(
                request.POST.get(
                    'quantity',
                    1
                )
            )

            food = food_items.objects.get(
                id=food_id
            )

            cart, created = (
                Cart.objects.get_or_create(
                    customer=request.user
                )
            )

            try:

                item = (
                    cart_items.objects.get(
                        cart=cart,
                        food_item=food
                    )
                )

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

@login_required
def remove_from_cart(request, item_id):

    if not request.user.is_authenticated:
        return redirect('login')

    try:

        cart = Cart.objects.get(
            customer=request.user
        )

        item = cart_items.objects.get(
            id=item_id,
            cart=cart
        )

        item.delete()

    except (
        Cart.DoesNotExist,
        cart_items.DoesNotExist
    ):
        pass

    return redirect('cart')