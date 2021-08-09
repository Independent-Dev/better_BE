from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='amqp://localhost')

# routing과 관련이 있는 부분
app.conf.update(
    task_routes={
        'tasks.add': {'queue': 'add'},
        'tasks.mul': {'queue': 'mul'}
    },
)

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y