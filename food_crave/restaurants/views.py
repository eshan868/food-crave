from django.shortcuts import render, redirect, get_object_or_404
from .forms import food_items_form, Restaurant_form
from .models import Restaurant, food_items
from orders.models import Order
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def restaurant_dashboard(request):
    restaurants = Restaurant.objects.filter(owner=request.user)

    foods = food_items.objects.filter(restaurant__owner=request.user)

    orders = Order.objects.filter(restaurant__owner=request.user).order_by(
        "-created_at"
    )

    total_restaurants = restaurants.count()

    total_foods = foods.count()

    total_orders = orders.count()

    pending_orders = orders.exclude(status="delivered").count()

    delivered_orders = orders.filter(status="delivered").count()

    revenue = sum(order.total_price for order in orders.filter(status="delivered"))

    return render(
        request,
        "restaurants/restaurant_dashboard.html",
        {
            "restaurants": restaurants,
            "foods": foods,
            "orders": orders[:10],
            "total_restaurants": total_restaurants,
            "total_foods": total_foods,
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "delivered_orders": delivered_orders,
            "revenue": revenue,
        },
    )


@login_required
def add_food(request):

    if request.method == "POST":

        form = food_items_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("restaurant-owner-dashboard")

    else:
        form = food_items_form()

    return render(request, "restaurants/add_food.html", {"form": form})


@login_required
def add_restaurant(request):

    if request.method == "POST":

        form = Restaurant_form(request.POST, request.FILES)

        if form.is_valid():

            restaurant = form.save(commit=False)

            restaurant.owner = request.user

            restaurant.latitude = request.POST.get("latitude")

            restaurant.longitude = request.POST.get("longitude")

            print(request.POST)
            restaurant.save()

            print("Restaurant Created")
            return redirect("restaurant-owner-dashboard")

    else:
        form = Restaurant_form()

    return render(request, "restaurants/add_restaurant.html", {"form": form})


def food_display(request):
    food = food_items.objects.all()

    return render(request, "food_items/food_display.html", {"foods": food})


def food_detail(request, food_id):

    food = get_object_or_404(food_items, id=food_id)

    return render(request, "food_items/food_detail.html", {"food": food})


def all_restaurants(request):

    restaurants = Restaurant.objects.all()

    return render(
        request, "restaurants/all_restaurants.html", {"restaurants": restaurants}
    )


def restaurant_detail(request, id):

    restaurant = get_object_or_404(Restaurant, id=id)

    foods = food_items.objects.filter(restaurant=restaurant)

    return render(
        request,
        "restaurants/restaurant_detail.html",
        {"restaurant": restaurant, "foods": foods},
    )


@login_required
def edit_restaurant(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, id=restaurant_id, owner=request.user)

    if request.method == "POST":

        form = Restaurant_form(request.POST, request.FILES, instance=restaurant)

        if form.is_valid():

            form.save()

            return redirect("restaurant-owner-dashboard")

    else:

        form = Restaurant_form(instance=restaurant)

    return render(request, "restaurants/edit_restaurant.html", {"form": form})


@login_required
def delete_restaurant(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, id=restaurant_id, owner=request.user)

    restaurant.delete()

    return redirect("restaurant-owner-dashboard")


@login_required
def edit_food(request, food_id):

    food = get_object_or_404(food_items, id=food_id, restaurant__owner=request.user)

    if request.method == "POST":

        form = food_items_form(request.POST, request.FILES, instance=food)

        if form.is_valid():

            form.save()

            return redirect("restaurant-owner-dashboard")

    else:

        form = food_items_form(instance=food)

    return render(request, "restaurants/edit_food.html", {"form": form})


@login_required
def delete_food(request, food_id):

    food = get_object_or_404(food_items, id=food_id, restaurant__owner=request.user)

    food.delete()

    return redirect("restaurant-owner-dashboard")
