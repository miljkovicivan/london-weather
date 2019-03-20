from django.db import models


class Weather(models.Model):

    temp = models.DecimalField(decimal_places=2, max_digits=10)
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    temp_min = models.DecimalField(decimal_places=2, max_digits=10)
    temp_max = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
