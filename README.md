# Food Crave 

## you can take a test of this website : https://food-crave-b5sj.vercel.app/

<img src="food_crave\static\images\home_page.jpeg" width="300">

This is a food delivery app made with python Django there are many apps like this, but this is my first project I am doing after learning the python Django. This app contains 3 different types of account "Restaurant owner, customer, deliver man " you can register to these types of accounts and do thing according to the type of your account.

## working of Food Crave 

> [!IMPORTANT]
> Allow location to this site because it will use coordinates to locate the restaurant and full time when user logged if the account type is delivery man so it may cause to error if you don't give location access.


the working of this website you experience depends based on the account type you created " Restaurant owner, customer and delivery man "
## If Account Type is Restaurant Owner 
once logged as a restaurant owner you will be taken to the dashboard of restaurant owner the followed things are the features:
### Dashboard
where you can see the summery of entire details of the things happening one the account, it can show all the restaurants you added, all the food you added, display total number of orders and total revenue up to that time. The owner got and there you can edit/delete the added restaurants or foods that are added and in navbar and in dashboard you will get the buttons to go to the pages 
### Add Food Item
To add food these requirements are necessary:
* Name
* Restaurant selection
* Description
* Photo
* Price
### Add Restaurant 
To Add restaurant these are the requirements 
* Name
* Address
* Photo

The restaurant Owner has also the features of the customers like ordering food view recent orders ect..
## If Account Type is Customer
* In customer account nav bar there it will have 5 options homepages, foods, restaurants, cart and my orders.
* Once logged as customer, you will be directly taken to the foods page the features for customers is listed below:
### Food Display Page 

* Can use the search bar located in the navbar to search food item or you can scroll to bottom. 
* Every food item is displayed with its:
    * Image
    * Name
    * Price
* It comes with 3 options add to cart and view details and quantity
### 1. View Details

* Foods are displayed with its:
     * Image
     * Name
     * Price
     * Description
     * The restaurant that belongs
* If the add to cart is chosen it will directly add to cart
### 2. Add To Cart 
* In this page the below listed task can done:
     * Delete
     * Proceed To Checkout
  
* Here it will display:
     * All to items added
     * Total price
* In proceed to checkout were usual we will integrant the payment method but since I due to some problem I cannot add payment integration 
* In checkout page it displays:
     *  All items to by
     *  Total amount to pay including GST and everything
     *  Address to deliver
* A button called Place order then the order will be placed and re direct to My orders
### My Orders  
it will display all the recent orders along with these following things:
     * OTP will be displayed
     * Status like placed, picked up, delivered

### Restaurant Display Page 

* It will be displaying all the restaurants along with these things:
     * Name
     * Image
     * Address
     * Button called visit and if that pressed and directed to a page were its address and name and all the foods in that restaurant          and from there also the food can order 

## If Account Type is Delivery Man
* Once logged then it will directly take to the dashboard almost like restaurant dashboard but here it displays
     * All the orders that are accepted 
     * The total earnings
     * Targets like goals with progress bar
     * Rating
     * Completed orders
* It has two option like go online and new order
### New Orders
* In new orders it will be displayed all the orders that are not accepted along with the following things:
     * Customer name 
     * Customer address 
     * Restaurant name 
     * Customers address
     * Total earnings
     
* When order is accepted then it will have two options like picked up and navigate restaurant if the navigate to restaurant is choose
     * it will take to google map were the locations are filled automatically lit is done by URL like but filled the address                   provided by restaurant owner and customer .And they can drive to the restaurant like and from there
* if they choose piked up
     * then the status and will become picked up and ask for OTP that previously provided to customer while placing the order after            entering the OTP correctly then only the order will consider as placed .

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
