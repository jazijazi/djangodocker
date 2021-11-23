from djangodocker.celery import app
from celery.utils.log import get_task_logger
import sys
from django.core.management import call_command
from celery import shared_task

from .email import send_email

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@app.task(autoretry_for=(Exception,),retry_kwargs={'max_retries':3} ,
                retry_backoff=True , retry_backoff_max=10 , retry_jitter=True) #backoff >> for avoid overwhelming // jitter >> for randomness
def send_email_task(name , email , body):
    logger.info("Sent email")
    return send_email(name , email , body)

#@shared_task
@app.task()
def bkup():
    logger.info("CREATING A BACKUP FROM DATABASE")
    sys.stdout = open('db.json' , 'w')
    call_command('dumpdata' , 'auth') #auth ==> name of  model to backup

@app.task()
def add(a,b):
    logger.info("Add to integer")
    return a + b