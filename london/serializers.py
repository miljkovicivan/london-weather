from rest_framework import serializers

from london.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('temp', 'pressure', 'humidity', 'temp_min', 'temp_max')
