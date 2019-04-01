from django.conf.urls import url, include
from django.contrib import admin

from messaging import views as messaging_views
from web import views as web_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('web.urls', namespace='web'), name='home'),
    url(r'^messaging/$', include('messaging.urls', namespace='messaging'), name='messaging'),
    url(r'^notify/send_notification/', view=messaging_views.send_to_topic, name='send_notification'),
]
