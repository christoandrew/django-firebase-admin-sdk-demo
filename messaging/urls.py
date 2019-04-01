from django.conf.urls import url

from messaging import views

urlpatterns = [
    url('^$', view=views.index, name='index'),
    url('^register_device/$', view=views.register_device, name='register_device')
]