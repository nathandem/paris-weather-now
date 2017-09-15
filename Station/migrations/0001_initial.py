# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_url', models.URLField()),
                ('weather', models.CharField(max_length=100)),
                ('temp_c', models.FloatField()),
                ('feelslike_c', models.FloatField()),
                ('precip_today_string', models.CharField(max_length=100)),
                ('wind_string', models.CharField(max_length=100)),
                ('relative_humidity', models.CharField(max_length=100)),
                ('observation_time', models.CharField(max_length=100)),
            ],
        ),
    ]
