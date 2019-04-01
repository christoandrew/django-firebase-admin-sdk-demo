# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from tasks import deliver_notification


class Entity(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Entities'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    registration_token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.registration_token

    def __unicode__(self):
        return self.registration_token


@receiver(post_save, sender=Entity, dispatch_uid='send_notification')
def send_notification(sender, instance, **kwargs):
    deliver_notification.delay("entity", value=instance.name)
