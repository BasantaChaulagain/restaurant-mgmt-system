from django.conf.urls import url
from . import views

app_name = 'public'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order/$', views.order, name='order'),
    url(r'^serve/$', views.serve, name='serve'),
    url(r'^cook/$', views.cook, name='cook'),
    url(r'^pay/$', views.pay, name='pay'),
    url(r'^manager/$', views.manager, name='manager'),
    url(r'^contact/$', views.contact, name='contact'),
]