# FoodCrave — Food Delivery Platform

## A fully functional Food Delivery Platform with three types of accounts role Restaurant,delivery_man,customers

## Project Overview

This project is a full-stack food delivery web application developed using django. The platform allows customers to order food online, restauarant owners to manage restaurant and food items, and delivery partners to handle deliveries

##Features

## Customer

Customers can:

Register account
Login and logout
Edit profile
Upload profile picture
Browse restaurants
Search food items
View restaurant details
Add items to cart
Update cart quantity
Checkout orders
Place orders
View order history
Track order status

## Restaurant Owner

Restaurant owners can:

Create restaurant
Update restaurant details
Upload restaurant image
Add food items
Edit food details
Delete food items
Manage menu
View customer orders
Access restaurant dashboard

##Delivery Partner

Delivery partners can:

Register as delivery partner
View available deliveries
Accept delivery requests
Navigate to destination
Verify delivery OTP
Update delivery status
Complete delivery

## Order Workflow

Customer

↓

Browse Restaurants

↓

View Food Items

↓

Add To Cart

↓

Checkout

↓

Place Order

↓

Restaurant Receives Order

↓

Delivery Partner Accepts Order

↓

OTP Verification

↓

Order Delivered

## Tech Stack

Backend:

Django

Database:

PostgreSQL (Neon)

Media Storage:

Cloudinary

Hosting:

Vercel

Static Files:

WhiteNoise

Frontend:

HTML
CSS
JavaScript

## Installation

Clone Repository
git clone https://github.com/eshan868/food-crave.git

Move into project:

cd food_crave

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure environment variables:

SECRET_KEY=<your_secret_key>

DATABASE_URL=<your_database_url>

CLOUDINARY_CLOUD_NAME=<cloudinary_cloud_name>
CLOUDINARY_API_KEY=<cloudinary_api_key>
CLOUDINARY_API_SECRET=<cloudinary_api_secret>

Apply migrations:

python manage.py migrate

Collect static files:

python manage.py collectstatic

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
