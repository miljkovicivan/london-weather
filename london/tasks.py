import requests
import json
import os


def get_weather():
    from london.models import Weather
    url = "http://api.openweathermap.org/data/2.5/weather?q=London,Uk"
    headers = {'x-api-key': os.getenv('OPEN_WEATHER_MAP_X_API_KEY')}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)['main']

    Weather.objects.create(**data)
