from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
    path(
        "remove-item-from-cart/<int:item_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),
    path("checkout/", views.checkout, name="checkout"),
    path("oder-history/", views.order_history, name="order_history"),
    path("place-order/", views.place_order, name="place_order"),
]
