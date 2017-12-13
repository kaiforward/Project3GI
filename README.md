# Project3GI

Browser based online trading game

## Overview

### What is this site for?

This site is an web-based browser trading game in the setting of a fictional sci-fi galaxy.

### What does it do?

This site will allow user to create an account and take part in a fictional galactic trading simulation. They will be able to purchase and trade different elements, buy ships to move them and mines to create them. They will be able to Trade them with companies (other players) and planets which players can sell to. Players can set their own prices for elements, and planet prices change as players buy from them.

### How does it work?

This site will use a Django back-end framwork using an SQL database. The front end will make use of bootstrap and jquery for extra functionality as well as basic forms.

## Tech Used

### Some the tech used includes:
- [Bootstrap](http://getbootstrap.com/)
    - I use **Bootstrap** to include some useful layout functionality like tabs.
- [JQuery](https://jquery.com/)
  - **JQuery** is used for extra front-end functionality.
- [Django](https://www.djangoproject.com/)
    - This project runs a Django 1.11 framework.
- [PostGreSQL](https://www.postgresql.org/)
    - This site uses Heroku's PostGreSQL add-on for the user database as well as SQLite while in development.
  
## Contributing

### On local machine.

Firstly you will need to clone this repository by running the git clone <project's Github URL> command

This project uses Python version 2.7.14
- [Python 2.7.14](https://www.python.org/downloads/)

Using VirtualENV create a virtual enviroment and navigate to the requirements folder inside the root folder of the project.

using pip install the requirments in dev.txt using 
```
pip install -r dev.txt
```

Now navigate back to the project root folder, and run:

```
python manage.py runserver
```
This should start a server on Localhost, if you make any changes you think should be in the project submit a pull request!

## Deployment

After finishing the project and having it run on a local machine i need to move the project onto Heroku. Firstly i signed up to [Heroku](https://signup.heroku.com/) and then [installed](https://devcenter.heroku.com/articles/heroku-cli) it. Then I created a new Heroku app from the Heroku dashboard.

With my VirtualEnv activated, I Then installed gunicorn from the command line using:
```
pip install gunicorn
```

I then moved to serperate my development code from production code by seperating my settings.py file into a base.py for dependencies needed by both development servers and productions. dev.py and staging.py contained settings for development and production servers respectively.

The important things to change were to move Strip, Paypal and Database settings from base.py to dev.py and staging.py, dev.py will contain test paypal, stripe and database settings, and staging.py will contain the same details but suitable for live production. i.e a live PayPal key.

We also do the same with the requirements files, where base.txt contains most of the dependencies. Dev.txt will contain dependencies only need for development and staging.txt will contain whats is needed for a live production server, for example SQL databases.

### Procfiles

Next week need to create our procfiles, in Procfile we include the following:
```
web: gunicorn we_are_social.wsgi:application
```
we also add a runtime.txt to tell which python version we are using:
```
python-2.7.14
```
Then we create the Procfile.Local for running the server locally with heroku.

for windows it looks like this 
```
web: python manage.py runserver
```
and on mac
```
web: gunicorn we_are_social.wsgi:application
```

Then by using the following command we should be able to open the server locally.
```
heroku local -f Procfile.local
```

### Heroku

Next we head back to heroku, and connect our github repository with our heroku app and enable automatic deploy's so any future pushes to git will be reflected in the heroku app.

To change the settings heroku uses when running the server use: 
```
heroku config:set DJANGO_SETTINGS_MODULE=settings.staging --app YOUR_HEROKU_APP
```
To stop static file errors until whitenoise is installed we can use:
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app YOUR_HEROKU_APP
```
then run:
```
heroku ps:scale web=1 --app YOUR_HEROKU_APP
```

### ClearDB MySQL

To use ClearDB, head to the resources tab for the django app and choose Cleardb in the add-ons sections.

So that we can use the DB we have add another dependency to to staging.py and we are only using this for the live production server.
I did this by adding the following:
```
dj-database-url==0.2.1
```

The change staging.py to use the new Db setting.

```python
import dj_database_url
 
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}
```

After all these changes we can push all out migrations to Heroku by using the following command:
```
heroku run --app YOUR_HEROKU_APP python manage.py migrate --settings=setting.staging
```

To populate the database with objects we have already created we use this command to extract the data:
```
python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission --indent=4 > db.json --settings=settings.dev
```
Then this command to upload the data to the heroku server
```
heroku run --app YOUR_HEROKU_APP python manage.py loaddata db.json --settings=settings.staging
```
### Static Files

The last thing to do is ensure my staticfiles can be used on the server!

firstly i install whitenoise:
```
pip install -r requirements/base.txt
```

Then modify the WSGI file with the following:

```python
import os
 
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.staging")
 
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```
This wraps the application in a whitenoise function which allows it to acess the staticfiles and serve them.

Last but not least we have to remove our DISABLE_COLLECTSTATIC command from heroku by either going to the ConfigVars on heroku and remove it, or input the following command:
```
heroku config:unset DISABLE_COLLECTSTATIC=1 --app YOUR_HEROKU_APP
```

The site is now viewable on Heroku!












