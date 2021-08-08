from celery import Celery
from time import sleep

app = Celery('tasks', backend='redis://localhost', broker='amqp://localhost')

@app.task
def add(x, y):
    sleep(10)
    return x + y