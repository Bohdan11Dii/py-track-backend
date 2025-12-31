import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pytrack_python.settings')

app = Celery('pytrack_python')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

