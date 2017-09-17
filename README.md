# Goal

Simple webapp whose only mission is to give the current weather in Paris, France.

# Approach

Weather data is provided by [Weather Underground](https://www.wunderground.com/) through their private API (free plan).

In order not to burn the API calls limit (10 calls/min), a worker is used to fetch fresh data every 10min and store them in a postgres table. So each time a new user comes to the site, he/she doesn't consume an API call, instead there's just a SQL request made to the DB (via Django built-in ORM).

The worker is separated from the rest of the django code, so that it remains in plain python and can be triggered more easily by a scheduler (a simple bash worker provided by Heroku).

Sensitive information (django keys, DB credentials and API token) are stored in a hidden file (keys.py) imported wherever needed.

# Built with

[Django](https://www.djangoproject.com/) - A python web framework<br/>
[Request](http://docs.python-requests.org/) - A python lib to deal with REST APIs<br/>
[Gunicorn](http://gunicorn.org/) - A light-weight, python WSGI<br/>
& the app is deployed on [Heroku](http://heroku.com/)
