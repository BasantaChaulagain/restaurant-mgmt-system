import datetime

from django.db import models
from django.utils import timezone

class Stock(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date bought')
    qtt = models.IntegerField()
    rate = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    