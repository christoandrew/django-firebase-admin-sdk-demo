from django.conf.urls import url
from django.contrib import admin

from messaging import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', view=views.index, name='notify'),
    url(r'^notify/send_notification/', view=views.send_to_topic, name='send_notification'),
]
