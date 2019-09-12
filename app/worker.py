import os
from celery import Celery


app = Celery(include=('tasks',))
app.conf.beat_schedule = {
    'refresh': {
        'task': 'refresh',
        'schedule': 10,
        'args': (12, 34, 56)
    },
}

