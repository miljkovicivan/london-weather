from django.urls import path

from london.views import weather_view, index


urls = [
    path('', index, name='index'),
]


api_urls = [
    path('london', weather_view),
]
