from __future__ import absolute_import
from .celery import app
import time

#app is used as a decorator

@app.task
def longtime_add(x, y):
    '''
    This will simulate a task that is will take a bit of time.
    Once time has elapsed it will add the two params together.

    :param x: first number
    :param y: second number
    :return: sum
    '''
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
    return x + y