from django.db import models

# need to import our fetched api data

class Reading(models.Model):
    icon_url = models.URLField()
    weather = models.CharField(max_length=100)
    temp_c = models.FloatField()
    feelslike_c = models.FloatField()
    precip_today_string = models.CharField(max_length=100)
    wind_string = models.CharField(max_length=100)
    relative_humidity = models.CharField(max_length=100)
    observation_time = models.CharField(max_length=100)
