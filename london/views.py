from rest_framework import generics

from london.models import Weather
from london.serializers import WeatherSerializer


class WeatherView(generics.RetrieveAPIView):

    serializer_class = WeatherSerializer

    def get_object(self, *args, **kwargs):
        return Weather.objects.last()


weather_view = WeatherView.as_view()
