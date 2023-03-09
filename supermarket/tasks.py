
from signscloud.celery import app
from supermarket.models import Stores, Deals
import time
from django.core.mail import send_mail
from .serializer import UserSerializer, DealSerializer
from django.template import loader

from pathlib import Path
import os

@app.task
def sendEmailToSubscribers():
    stores = Stores.objects.all()
    for s in stores:
        users = UserSerializer(s.users, many=True).data
        for u in users:
            
            if len(u) > 0:
                try:
                    deals = Deals.objects.filter(store_id=s.id)
                    dealsDict = DealSerializer(deals, many=True).data
                except Deals.DoesNotExist:
                    dealsDict = []
                
                html_message = loader.render_to_string(
                '/app/templates/supermarket/email.html',{
                'first_name': u['first_name'],
                'last_name': u['last_name'],
                'deals': dealsDict,
                'email': u['email'],
                'store_name': s.name,
                'subject':  'Ofertas Especiales solo para ti'})
                send_mail(
                    subject='Ofertas Especiales solo para ti.',
                    message='',
                    from_email='from@example.com',
                    recipient_list=[u['email']],
                    fail_silently=False,
                    html_message=html_message
                )