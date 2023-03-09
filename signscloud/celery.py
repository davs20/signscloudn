#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Queue tasks for batch processing and parallel processing
#

# Queue handler
from celery import Celery
from celery.schedules import crontab
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signscloud.settings')
app = Celery('signscloud', broker='redis://redis:6379')
#app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: ')
    
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-to-subscribers': {
        'task': 'supermarket.tasks.sendEmailToSubscribers',
        'schedule': crontab(hour=10, minute=30, day_of_week=1),
        #'schedule': 10,
        
        'args': ()
    },
}

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, waitNSeconds.s(30), name='add every 10')

#     # Calls test('world') every 30 seconds
#     # sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(
#     #     crontab(hour=7, minute=30, day_of_week=1),
#     #     test.s('Happy Mondays!'),
#     # )


