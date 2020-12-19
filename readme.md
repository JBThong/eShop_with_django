This is the source code for the eShop.


Installation
============
Software installation
----------------------

You will need to install several things first:

* Python 3.7
* PostgreSQL 11.7 or later. Earlier versions might work, but are untested.

With these requirements installed you can create a virtual environment to install
all required Python packages:
- With Linux system
```sh
   $ cd eShop
   $ python3.7 -m venv env
   $ source bin/activate
   $ pip install -r requirements.txt
```
- With Windown system
```sh
   $ python -m venv ./env
   $ env\Scripts\activate 
   $ pip install -r requirements.txt
```

Database setup
--------------
Change config DATABASES in eShop/eShop/settings.py. Run command below to migrate database 
```sh
    $ python manage.py migrate
```

Start appp
--------

For local development environment:

- With Windown system:
```sh
  $python manange.py runserver
```

- With Linux system:
```sh
  $python3 manange.py runserver
```