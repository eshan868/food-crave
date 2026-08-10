# Food Crave 

## you can take a test of this website : https://food-crave-b5sj.vercel.app/

<img src="food_crave\static\images\home_page.jpeg" width="300">

This is a food delivery app made with python Django there are many apps like this, but this is my first project I am doing after learning the python Django. This app contains 3 different types of account "Restaurant owner, customer, deliver man " you can register to these types of accounts and do thing according to the type of your account.

## working of Food Crave 

> [!IMPORTANT]
> Allow location to this site because it will use coordinates to locate the restaurant and full time when user logged if the account type is delivery man so it may cause to error if you don't give location access.


the working of this website you experience depends based on the account type you created " Restaurant owner, customer and delivery man "
if you logged as a restaurant owner you will be taken to the dashboard of restaurant owner where you can see the summery of entire details of the things happening one the account, it can show all the restaurants you added, all the food you added, display total number of orders and total revenue up to that time  that owner got and there you can edit/delete the added restaurants or foods that are added and in navbar and in dashboard you will get the buttons to go to the pages to add a restaurant or add food  they can add restaurant/food by the requirements required like name, description, photo, for food it will be price and for restaurant it will be address. And the restaurant order has also the features that has to the customers like ordering food view recent orders ect..

if you logged as customer, you will be directly taken to the foods page where you can use the search bar located in the navbar to search food item or you can scroll to bottom. in nav bar it will have 5 options homepages, foods, restaurants, cart and my orders. in foods page in every food item its image, name and price will be displayed with 3 options add to cart and view details and quantity change like how much need and if the option view details is pressed then a page will open where it will display it image, name, price, its description and the restaurant that belongs and if the add to cart is chosen it will directly add to car and in cart page you can delete the item and it will show the all to items added and total price and a button to proceed to checkout were usual we will integrant the payment method but since I due to some problem I cannot add payment integration so it will proceed to checkout page were you can see the items to by  the total amount to pay including GST and everything then the address to deliver then the order will be placed. and in my orders the order can see and there the OTP will be displayed and the status like placed, picked up, delivered
ad in restaurant page there it will be displayed all the restaurants displayed like foods but with button visit and if that pressed and directed to a page were its address and name and all the foods in that restaurant and from there also, can order 

if logged in as delivery man then it will directly take to the dashboard almost like restaurant dashboard but here it displays all the orders that are accepted and it will be displayed the total earnings targeted like goals with progress bas and rating and completed orders and it has two option like go online and new order in new orders it will be displayed all the orders that are not accepted in that it will be displayed the customer name and their address and restaurant name and its address and the total earnings ad if the order is accepted then it will have two options like picked up and navigate restaurant if the navigate to restaurant is choose then it will take to google map were the locations are filled automatically lit is done by URL like but filled the address provided by customer and dashboard and they can drive to the restaurant like and from there if they choose piked up then the status and will become picked up and ask for OTP that previously provided to customer while placing the order after entering the otp correctly then only the order will consider as placed .

## instructions to build

Follow these steps to build run the website on your local machine.

1. fork this repository then open your terminal and run:

        git clone <YOUR_REPOSITORY_URL>

2. move into the project folder inside that another folder will be there then move into that in that 

3. Create a Python virtual environment:

         python -m venv venv

4. Activate it:

   if Windows:

         venv\Scripts\activate

   if macOS / Linux:

          source venv/bin/activate

5. then Install the required Python packages:

          pip install -r requirements.txt

6. then Run the Django migrations:

          python manage.py migrate

7. Start the Django development server:

          python manage.py runserver

8. Open the website in your browser:

   http://127.0.0.1:8000/
