import os

CELERYD_PREFETCH_MULTIPLIER = int(os.environ.get('CELERYD_PREFETCH_MULTIPLIER') or '100')
CELERYD_TASK_SOFT_TIME_LIMIT = int(os.environ.get('CELERYD_TASK_SOFT_TIME_LIMIT') or '3600')
CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_IMPORTS = (
    'celery_test.tasks',
)

BROKER_URL = 'amqp://guest:guest@rabbitmq:5672'
