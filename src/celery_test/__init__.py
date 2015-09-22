import os

from celery import Celery

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_test.config')

app = Celery('celery_test')
app.config_from_envvar('CELERY_CONFIG_MODULE')
