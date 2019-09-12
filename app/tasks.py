from celery.utils.log import get_task_logger
from worker import app
import time
import random


logger = get_task_logger(__name__)


@app.task(bind=True, name='refresh')
def refresh(self, *args):
    for num in args:
        logger.info(f'Working on arg: {num}')



@app.task(bind=True, name='batch')
def batch_task(self, id):
    logger.info(f'Working on task id: {id}')
    time.sleep(random.randint(5, 10))
    logger.info(f'Task id: {id} done')


