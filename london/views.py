from rest_framework import generics
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


from london.models import Weather
from london.serializers import WeatherSerializer


class WeatherView(generics.RetrieveAPIView):

    serializer_class = WeatherSerializer

    def get_object(self, *args, **kwargs):
        return Weather.objects.last()



weather_view = WeatherView.as_view()


def index(request):
    obj = Weather.objects.last()
    context = {'obj': obj}
    return render(request, 'london/index.html', context)
