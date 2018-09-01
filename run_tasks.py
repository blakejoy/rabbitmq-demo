from .tasks import longtime_add
import time

'''
call the longtime add method using a delay needed if the task
is going to run async

The 1 (x) and 2 (y) are the parameters that are being passed 
to the task.

result.ready() will return True if task complete.
result.result will return 3
'''

'''
BUG: pip install --upgrade https://github.com/celery/celery/tarball/master

There is an error that needs to be fixed with the naming of async module being
called in celery library for Python 3.7. This is a fix until they release the
update sometime soon.
'''

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    # at this time, our task is not finished, so it will return False
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)