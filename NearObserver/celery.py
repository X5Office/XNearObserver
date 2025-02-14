import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NearObserver.settings')
app = Celery('django', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',)
app.config_from_object('django.conf:settings', namespace='CALERY')
app.autodiscover_tasks()
