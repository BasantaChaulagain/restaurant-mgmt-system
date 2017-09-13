from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^salarydetails/$', views.salarydetails, name='salary_details'),
]
