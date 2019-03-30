import firebase_admin
from django.conf import settings
from firebase_admin import credentials

from celery import app as celery_app

__all__ = ('celery_app',)
cred = credentials.Certificate(settings.CERTIFICATE_PATH)
default_app = firebase_admin.initialize_app(cred)
