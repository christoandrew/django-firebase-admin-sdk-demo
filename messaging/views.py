# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from firebase_admin import messaging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'messaging/index.html')


def register_device(request):
    pass


def send_to_topic(request):
    if request.method == 'POST':
        # [START send_to_topic]
        # The topic name can be optionally prefixed with "/topics/".
        topic = 'highScores'

        # See documentation on defining a message payload.
        message = messaging.Message(
            data={
                'score': "23",
                'time': timezone.now(),
            },
            topic=topic,
        )

        # Send a message to the devices subscribed to the provided topic.
        response = messaging.send(message)
        print "Response", response
        # Response is a message ID string.
        #
        return HttpResponseRedirect(reverse('notify'))
    else:
        print "Ditching request"
        return Http404
