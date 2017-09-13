import datetime

from django.db import models
from django.utils import timezone


class Table(models.Model):
    tableNum = models.IntegerField()
    def __str__(self):
        return str(self.tableNum)


class Constant(models.Model):
    serviceCharge = models.IntegerField()
    vat = models.IntegerField()
    def __str__(self):
        return str(self.vat)

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Food(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default=False)
    
    def __str__(self):
        return self.title

class Ordered_food(models.Model):
    title = models.CharField(default='null', max_length=200)
    category = models.ForeignKey(Category, default='null', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    table = models.ForeignKey(Table, default=1, on_delete=models.CASCADE)
    time = models.DateTimeField('time ordered') 
    is_served = models.BooleanField(default=False)
        
    def __str__(self):
        return self.title
    
    def ordered_today(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class Served_food(models.Model):
    title = models.CharField(default='null', max_length=200)
    category = models.ForeignKey(Category, default='null',on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    table = models.ForeignKey(Table, default=1, on_delete=models.CASCADE)
    time = models.DateTimeField('time served') 
    is_paid = models.BooleanField(default=False)
        
    def __str__(self):
        return self.title

    def served_today(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)
    
    
class Paid_food(models.Model):
    title = models.CharField(default='null', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    table = models.ForeignKey(Table, default=1, on_delete=models.CASCADE)   
    time = models.DateTimeField('time paid') 
        
    def __str__(self):
        return self.title
    
    def paid_today(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)
    