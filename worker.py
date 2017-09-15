import requests
import psycopg2
from datetime import datetime
import logging

# api-token & db password
from keys import *

def fetch_data():
    # connection to api
    url = "http://api.wunderground.com/api/" + WU_API_TOKEN + "/conditions/q/France/Paris.json"
    r = requests.get(url).json()
    data = r['current_observation']

    # DATA TAKEN FROM THE API
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
    # observation_time = data['observation_time']

    # if via Django's ORM
    # r = Reading(icon_url=icon_url,weather=weather)
    # r.save()
    # needed? https://stackoverflow.com/questions/8951255/import-script-from-a-parent-directory

    # open db
    try:
        conn = psycopg2.connect(dbname=DB_NAME,
        user=DB_USER,
        host=DB_HOST,
        password=DB_PASSWORD,
        port=DB_PORT)
    except:
        print("Unable to open the db at "+datetime.now())
        logging.exception("Unable to open the db at "+datetime.now())
        return # putting a blank except return in a function is an easy way to stop an execution
    else:
        cur = conn.cursor()

    # write data to db
    cur.execute("""INSERT INTO "Station_reading" (icon_url,weather,temp_c,feelslike_c,precip_today_string,wind_string,relative_humidity,observation_time)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", (icon_url,weather,temp_c,feelslike_c,precip_today_string,wind_string,relative_humidity,observation_time))
    conn.commit()

    # close db
    cur.close()
    conn.close()

    # print("Data written ",datetime.now())

fetch_data()
