from celery.utils.log import get_task_logger
from worker import app


for i in range(10):
    app.send_task("batch", args=[i])
    print(f"Sent task {i}")
