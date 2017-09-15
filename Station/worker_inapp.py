import requests
from datetime import datetime
import logging

from Station.models import Reading

# api-token & db password

def fetch_data():
    api_token = fe85ddc2bf0deb5b
    url = "http://api.wunderground.com/api/" + api-token + "/conditions/q/CA/San_Francisco.json"
    r = requests.get(url).json()
    data = r['current_observation']

    # DATA TAKE FROM THE API
    # visual summary of the weather
    icon_url = data['icon_url']
    # core data: weather, temperature, precipitation, wind, humidity
    weather = data['weather']
    temp_c = data['temp_c']
    feelslike_c = data['feelslike_c']
    precip_today_string = data['precip_today_string']
    wind_string = data['wind_string']
    relative_humidity = data['relative_humidity']
    # meta
    observation_time = data['observation_time']

    # let's add the data to the db
    r = Reading(icon_url=icon_url,weather=weather)
    r.save()

    print("Data written ",datetime.now())

fetch_data()
