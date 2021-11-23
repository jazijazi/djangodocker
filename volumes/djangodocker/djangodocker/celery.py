from celery import Celery
import celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'djangodocker.settings') #for call command

app = Celery('djangodocker')

app.config_from_object('django.conf:settings' , namespace="CELERY")

app.autodiscover_tasks()