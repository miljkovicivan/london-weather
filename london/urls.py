from django.urls import path

from london.views import weather_view


api_urls = [
    path('london', weather_view),
]
