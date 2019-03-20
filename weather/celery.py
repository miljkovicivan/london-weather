# coding=utf-8
"""
Celery Bootstrap
"""
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from london.tasks import get_weather



# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

app = Celery('weather')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(10 * 1.0, get_weather_task.s(), name='get weather')


@app.task
def get_weather_task():
    get_weather()
