import os

from kombu import Exchange, Queue

CELERYD_PREFETCH_MULTIPLIER = int(os.environ.get('CELERYD_PREFETCH_MULTIPLIER') or '0')
CELERYD_TASK_SOFT_TIME_LIMIT = int(os.environ.get('CELERYD_TASK_SOFT_TIME_LIMIT') or '60')
CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_IMPORTS = (
    'celery_test.tasks',
)
CELERY_ACKS_LATE = True
CELERY_ENABLE_REMOTE_CONTROL = False

CELERY_RDB_HOST = os.environ.get('CELERY_RDB_HOST') or '0.0.0.0'
CELERY_RDB_PORT = int(os.environ.get('CELERY_RDB_PORT') or '6900')

BROKER_URL = 'amqp://guest:guest@rabbitmq:5672'


CELERY_ROUTE_MAP = {
    'celery.default': {
        'tasks': [],
    },

    'celery.batch_exceptions': {
        'tasks': [
            'celery_test.tasks.batch_exceptions',
        ]
    },
    'celery.batch_exceptions_retries': {
        'tasks': [
            'celery_test.tasks.batch_exceptions_retries',
        ]
    },
    'celery.batch_timeout': {
        'tasks': [
            'celery_test.tasks.batch_timeout',
        ]
    },
}

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = [
    Queue(queue, Exchange('celery'), routing_key=queue) for queue in CELERY_ROUTE_MAP.iterkeys()
]

CELERY_ROUTES = {}
for queue, task_def in CELERY_ROUTE_MAP.iteritems():
    for task in task_def['tasks']:
        CELERY_ROUTES[task] = {'queue': queue, 'routing_key': queue}
