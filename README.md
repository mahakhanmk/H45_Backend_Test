# DRF\_Backend\_

## Introduction:

The Project is a **Django** project which is using the **Django Rest Framework**. This Django REST API project uses Postgres for CRUD operations and django-filter for filtering fields. The project also uses django-cors-headers to handle CORS and django-rest-framework for building REST APIs.

## Libraries Used:

The following libraries were used in this project:

- **django:** The core Django library was used to build the web application and implement its basic functionality.
- **psycopg2:** This library is required for Django to connect to PostgreSQL databases.
- **djangorestframework:** This library provides tools and utilities for building RESTful APIs in Django.
- **django-cors-headers:** This library allows cross-origin resource sharing (CORS) headers to be added to HTTP responses in Django.
- **django-filter:** This library provides a simple and powerful way to filter data in Django using the Django ORM.

## Endpoints:

The following endpoints are available:

1) #### /domain/driver/

- Returns a list of available drivers
- Allows filtering using a driver's email, mobile\_number, language, and their truck's number\_plate
- Allows creating a single driver by passing a list
- Allows creating bulk drivers in a list

2) #### /domain/driver/\<id\>

- Returns a single driver

## Setting Up Postgres on Local Machine:

To set up Postgres on a local machine after pulling this project from GitHub, follow these steps:

1. Install Postgres on your local machine.
2. Create a Postgres database for the project. ("apiDB" is the name used in the project.)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'apiDB',        #Enter your database name
        'USER': 'postgres',     #Enter your username
        'PASSWORD': 'XXXX',     #Enter database password
        'HOST': '127.0.0.1',
        'PORT': '5432',         #Change port if required
    }
}
```
3. Update the **DATABASES** setting in the **settings.py** file to use your Postgres database settings.
4. Run the migrations using the following command:
```
python manage.py migrate
```

## Potential Improvements:

1. Use class-based views instead of function-based views.
2. Use Django REST Swagger to document the API.
3. Add authentication and authorization to restrict access to certain endpoints.
4. Implement pagination to handle large datasets efficiently.

## Production Consideration:

When deploying this project to a production environment, the following considerations should be taken into account:

1. Set up environment variables for sensitive data such as database credentials.
2. Use a production-ready web server.
3. Proper security measures should be put in place, such as SSL/TLS encryption and secure authentication methods when they are added.

## Assumptions:

During the schema design phase of this project, the following assumptions were made:

- Each truck has a unique number\_plate and registration\_number.
- The application would not require extensive data validation or custom business logic beyond basic CRUD operations.
- The truck application would only require basic CRUD operations on its data to add trucks.

#### Note:
CRUD functions are also added to the TRUCK model for creating and deleting new TRUCKS. Please create a super user to use the admin panel to add data entries.
```
python manage.py createsuperuser
```
