from __future__ import absolute_import
from celery import Celery


'''
:param project_name - the name of project
:param broker - going to be the rabbitmq instance that is started within docker
it uses the default guest username/pwd along with localhost on port 15672
:param backend - where task results would be stored
:include module list - imported when Celery worker starts so tasks can be found
'''

'''
$ rabbitmqctl add_user username password

$ rabbitmqctl add_vhost virtual_host_name

$ rabbitmqctl set_user_tags username username_tag

$ rabbitmqctl set_permissions -p virtual_host_name username ".*" ".*" ".*"

the end of this command sets read write permissions for the user 
'''


'''
In a terminal you want to run this command from the parent directory of your python
project. It should connect and you will have started the celery service with the
modules you set in the include parameter.

celery -A project_name worker --loglevel=info

In another terminal window you want to run the following command from the parent directory
of the project.

python -m project_name.run_tasks

This will run the run_tasks.py file that initiates the celery tasks.
If you look at the first terminal window you will see when the worker 
recieves and executes the task. 

'''


'''
To sum everything up the tasks are created in the tasks.py file. They are then sent to
an exchange that will distribute it to the right queue. This all happens in rabbitMQ.
The task is then consumed by the celery workers and you can see the result in the second
terminal window.
'''


app = Celery('rabbitmq-demo',
             broker='amqp://blake:blake123@localhost/blake_vhost',
             backend='rpc://',
             include=['rabbitmq-demo.tasks'])