from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from .models import Stock
from .forms import StockForm


def index(request):
    stocks = Stock.objects.all()
    total = 0
    
    if request.method == 'POST':
        form = StockForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.price = instance.qtt * instance.rate
            instance.date = timezone.now()
            instance.save()  
            return HttpResponseRedirect(reverse('inventory:index'))
    else:
        form = StockForm()
    
    for stock in stocks:
        total = total + stock.price
            
    return render(request, 'inventory/index.html', {'form': form, 'stocks': stocks, 'total' : total})

