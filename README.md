#Gallivant Design 

Project Milestone Four - Code Institute

https://gallivantdesign.herokuapp.com/

Important! Due to time limit on AWS I could not upload images and other static files. Submitting what I have.

This app was developed Victoria Ben-Chivar which is the last project for the Code Institute Software Development diploma.
This website emulates a freelancing e-commerce website that provides existing designs and promotes the possibility to order custom designs per request.

## Table of contents

1. [UX](#UX)
    1. [Design process](#Design-process)
    2. [Fonts](#Colors)
    3. [Wireframes](#Wireframes)
2. [Features](#Features)
    1. [Accounts](#Accounts)
        1. [Register page](#Register-page)
        2. [Login page](#Login-page)
        3. [Profile page](#Profile-page)
        4. [Reset password](#Reset-password)
        5. [Logout](#Logout)
    2. [Home page](#Home-page)
    3. [Products page](#Products-page)
        1. [Product details](#Product-details)
    4. [Request a design](#Request-a-design)
    5. [Cart](#Cart)
    6. [Checkout](#Checkout)
    7. [Admin panel](#Admin-panel)
    8. [404 page](#404-page)
    9. [Features left to implement](#Features-left-to-implement)
3. [Technologies](#Technologies)
    1. [Tools](#Tools)
    2. [Libraries and frameworks](#Libraries-and-frameworks)
    3. [Languages](#Languages)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
6. [Credits](#Credits)
    1. [Media](#Media)
    2. [Code](#Code)

# UX

## Design process
The main goal of the website was to present a collection of design created by the admin and make them available to purchase. For a start the main product are posters, but this site should be able to even sell other design products. The whole design process was based on that goal. Altogether this is a simple homepage with access to buy produced designs and make a custom design orders by contacting the Designer/Admin. Users can view existing products, buy them and make order requests. To be able to add, delete and edit products advanced features such as authentication is required it refers to Superusers. 

The design allows the user to make minimum steps in order to purchase, view or order a product with the help och accessible CTAs and links. The user has quick access to search for an product or item and also add it to the cart, the checkout is quick and uses Stripe services that accepts credit cards. The admin platform is Django which allows a super user to control orders, users and items.

## Design choices
The design allows the user to make minimum steps in order to purchase, view or order a product with the help och accessible CTAs and links. The user has quick access to search for an product or item and also add it to the cart, the checkout is quick and uses Stripe services that accepts credit cards. The admin platform is Django which allows a super user to control orders, users and items. 

Every screen has a ‘Go to Top’ feature when the user scrolls. Pressing the button helps the user to reach the beginning of the page.

### Fonts
- Using web friendly font Lato (https://fonts.google.com/specimen/Lato#about). A proper font for reading in different screen sizes.

### Wireframes
The wireframes developed for this project was created first for a larger project that scoped to an MVP due to time limit. Designed for different platforms from mobile to Desktop. You can find it in https://github.com/VictoriaBC/gallivantdesign/blob/master/Wireframe_structure_inspiration_userstories.pdf

Wireframe was developed in Adobe XD

# Features

Here are the applications: `accounts`, `cart`, `checkout`, `products`, `home` and `orders`. Using Django framework, each application is a separate stand-alone module.

## Accounts
Users can create their account, log in and reset their password if needed. And Superusers can Edit, Add and Delete a product.    

### Register page
  -Username, e-mail and password are required to create an account.
  - Username must be unique.
  - Password must contain at least 8 characters.

### Login page
  - A username or email and password of an existing account are required to sign in.
  - Login credentials. Username: joshua-1 Password: YadiYada2956

### Profile page
  - For authenticated users. It provides a view of purchased products, download (not fully developed due to time limit on the project, should originally be able to download purchased product).

### Contact me and Order request
  - Anyone can type in their email and message to make an order request. The client will be then contacted to get more information needed.

### Reset password
  - Step 1: at the login page, you can find  `forgot my password` which will lead to a form to enter account e-mail.
  - Step 2: Add the e-mail from the account you need to reset the password.
  - Step 3: You will receive an email with a link that opens a new window that allows you to set a different password for your account.
  - Step 4: Once the password is set you can login with the new password.

### Logout
  - Logs out the currently authenticated user and clears the session.

## Home page
Home page introduces the user to Gallivant design and presented work. Leads to product page where all present design is presented and there is also a Hera with a CTA that leads the user to a request order/contact me page. The user has a main search function that leads to a page with products the contain searched word.

## Products page
Shows all products and the user can sort products according to alphabetical order and price. 

### Product details
Shows the product details, gives the user possibility to add the product to cart, add amount, read the products information, look at the image and even a larger image.

## Request a design
User requests an order by going to Custom Design. The user fills the form and submits a request.

## Cart
 From the cart page the user can click the CTA checkout that leads to Checkout page or keep shopping that leads to homepage. Also the user can have a brief look on chosen objects, remove them and add/decrease amount.  

## Checkout
  - The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality.

## Admin panel
The admin panel has 3 custom registered apps: Accounts, Orders and Products.

## 404 page

  - Custom styled 404 page, gives the user the ability to navigate back.


## Features Left To Implement
 1. Functional download
 2. Force user to register before proceeding to checkout
 3. Sell other products than poster
Sort order request to different categories
Layout more products on homepage


# Technologies

## Tools

  - [Stripe](https://stripe.com/ie) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [Github](https://github.com/) to share and store code remotely.
  - [Git](https://git-scm.com/) was used to manage version control.
  - [Sqlite3](https://www.sqlite.org/index.html) a database provided by django for development.
  - [PostgreSQL](https://www.postgresql.org/), a robust database provided by Heroku for production development.
  - Adobe XD for wireframe design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - Font awesome for the creation and implementation of icons.
  - [Google fonts](https://fonts.google.com/) to bring custom font styling.
  - [Jquery](https://jquery.com/) a Javascript library to simplify the code.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that enables python code to modify AWS service.

## Languages

  - The project uses HTML, CSS, Javascript and Python programming languages.


# Testing

Have not tested on real users, something to consider, but have gone through console and tested for responsiveness.

## Mobile
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 4
  - iPhone 5 SE
  - iPhone 6, 7 and 8
  - iPhone 6, 7 and 8 Plus (real device)
  - iPhone X

## Tablet
  - iPad
  - iPad Pro

## Laptop
  - Macbook

## Browsers
  - Chome
  - Safari
  - Firefox
  - Opera


# Deployment

To continue on the process of deployment you should have accounts on the following services:

  - [Stripe](https://stripe.com/ie)
  - [AWS](https://aws.amazon.com/s3/)
  - [Gmail](https://gmail.com)

### Instructions
  1. Download a copy of this repository from the link https://github.com/VictoriaBC/gallivantdesign as a download zip file. Or at your terminal do the following git command:

      ```
      $ git clone https://github.com/VictoriaBC/gallivantdesign

      ```
  2. If you downloaded the project as a zip file, unzip it and add it in your directory.

  3. To not run in some unexpected behaviours during development, a virtual environment is advised to be used before the project be installed in your machine. So create a virtual environment with the command:

      ```
     $ python -m venv venv
      ```
  4. After you already created the virtual environment folder you need to activate it:

      ```
      $ source venv/bin/activate
      ```
  5. Install requirements.txt file.

      ```
      $ pip install -r requirements.txt
      ```
  6. Create a `local_settings.py` file inside `freelancesolution` to store development variables:
     ```
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = <secret key>

    DEBUG = True

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    EMAIL_HOST_USER = <your gmail username>
    EMAIL_HOST_PASSWORD = <your gmail password>

    STRIPE_PUBLISHABLE = <Stripe publishable key>
    STRIPE_SECRET = <Stripe secret>
     ```

  7. Migrate the models to crete a database template.

      ```
      $ python manage.py migrate
      ```
  8. In this step you will need to create a super user to have access to the admin page.

      ```
      $ python manage.py createsuperuser
      ```
  9. So, after you do all the steps to create a super user you can now run the server.

      ```
      $ python manage.py runserver
      ```
  10. After the server is running locally add the `/admin` path at the end of the url link. It might look like this if you are not running another application.

      ```
      http://127.0.0.1:8000/admin
      ```

### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

  1. Signup for [Heroku](https://signup.heroku.com/)
  2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
  3. After installing `Heroku toolbelt` add the following code into your termial and login into your account you already create.
     ```
     $ heroku login
      Enter your Heroku credentials.
      Email: your@email.com
      Password (typing will be hidden):
      Authentication successful.
     ```
  4. Save all the requirements into the `requirements.txt` as mentioned before with the command:
     ```
     $ pip freeze > requirements.txt
     ```
  5. Create a file named `Procfile` and add the following config.
     ```
     release: python manage.py migrate
     web: gunicorn freelancesolution.wsgi:application
     ```
 6. After all the setup is done `git add .`, `git commit` and `git push` your application to a repository you created on Github.
 7. In your `Heroku`account click new and create new app.
 9. Select your region and create a name for your project.
10. In your `Heroku` settings click `reveal config vars`.
11. After adding the config into your dashboard add the following commands.
  - `$ heroku login`
  - `heroku git:remote -a test-app-to-deploy`
  - `$ git push heroku master`

14. On your `Heroku` dashboard click on `open app` button and check if the application is running correctly.
15. Login credentials. Username: joshua-1 Password: YadiYada2956
# Credits
Inspired by Alen Krga and Boutique Ado project in Code Institute course.

## Media
  - The photos used in the project were downloaded from personal library

## Code
  - The `accounts`, `cart` and `checkout` apps were recycled from the [Code Institute](https://github.com/Code-Institute-Org) lessons but modified to fit with the project purpose.
