# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from messaging.models import Entity, Topic

admin.site.register(Entity)
admin.site.register(Topic)