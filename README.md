# FoodCrave — Food Delivery Platform

## A fully functional Food Delivery Platform with three types of accounts role Restaurant,delivery_man,customers

## Project Overview

This project is a full-stack food delivery web application developed using django. The platform allows customers to order food online, restauarant owners to manage restaurant and food items, and delivery partners to handle deliveries

## Features 

## Customer

Customers can:

* Resgister
* Login 
* Edit profile 
* Browse restaurants
* Search foods
* Add food to cart
* place orders
* Track order history 

## Restaurant Owner 

Restaurant owner can:

* Create restaurants
* Edit restaurant details
* Add food items
* Update foods
* Delete foods
* Access dashboard

## Delivery Partner

Delivery partner can:

* View available orders
* Accept delivery
* Navigate using maps
* Verify OTP
* Complete delivery


## Workflow 

Customer

↓

Browse Restaurants

↓

View Foods

↓

Add To Cart

↓

Checkout

↓

Place Order

↓

Restaurant Receives Order

↓

Delivery Assigned

↓

Delivered

## Installation 

Clone repository:

git clone https://github.com/your-username/food-crave.git

Move into project:

cd food_crave

Create virtual environment:

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Install requirements:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run server:

python manage.py runserver

Open:

http://127.0.0.1:8000

## Preview

Home page

<img src="food_crave\static\images\home_page.jpeg" width="300">

Restaurant Dashboard

<img src="food_crave\static\images\restaurant_dashboard.jpeg" width="300">

Delivery Dashboard

<img src="food_crave\static\images\deliver_dashboard.jpeg" width="300">

Food Display

<img src="food_crave\static\images\food_display.jpeg" width="300">



## Admin Access


Create admin:

python manage.py createsuperuser

Open:

http://127.0.0.1:8000/admin/

## Future plans 


* Google Pay Integration
* Live Order Tracking
* AI Recommendations
* Notifications
* Ratings & Reviews

## Author 

Created by : Muhammed Eshan P 