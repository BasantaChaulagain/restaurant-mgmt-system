from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=500,default="ok")
    location = models.TextField(max_length=30,  default="Kathmandu")
    birthdate = models.DateField( default=timezone.now)
    salary = models.IntegerField(default=10000)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class attend(models.Model):
    a_user = models.ForeignKey(User,on_delete=models.CASCADE)
    a_date = models.DateField()
    a_time = models.TimeField()

    def __str__(self):
        return (self.a_user.username)


class salary (models.Model):
    s_user = models.ForeignKey(User,on_delete=models.CASCADE)
    s_paiddate = models.DateField()
    s_paidtime = models.TimeField()

    def __str__(self):
        return (self.s_user.username)
