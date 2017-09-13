from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from .models import Category, Food, Ordered_food, Served_food, Paid_food, Table
from django.db.models import Q
from .forms import ContactForm



def index(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    tables = Table.objects.all()
    query = request.GET.get("q")
    if query:
        foods = foods.filter(
            Q(title__icontains=query)
        ).distinct()
        categories = Category.objects.filter(food=foods)
        return render(request, 'public/index.html',{'foods': foods, 'categories':categories, 'tables':tables})
    else:  
         return render(request, 'public/index.html',{'foods': foods, 'categories':categories, 'tables':tables})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('public:index'))
    else:
        form = ContactForm()
    
    return render(request, 'public/contact.html', {'form': form})


def cook(request):
    foods = Ordered_food.objects.filter(is_served=False)
    served_foods = Served_food.objects.all()
    return render(request, 'public/cook.html',{'foods' : foods, 'served_foods' : served_foods})


def manager(request):
    served_foods = Served_food.objects.filter(is_paid=False)
    paid_foods = Paid_food.objects.all()
    total = 0
    for paid_food in paid_foods:
        total = total + paid_food.price
        
    return render(request, 'public/manager.html',{'served_foods' : served_foods, 'paid_foods' : paid_foods, 'total' : total})


def order(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    tables = Table.objects.all()
    orderd_food = Ordered_food()
    try:
        selected_food = foods.get(pk=request.POST['food'])
        selected_table = tables.get(pk=int(request.POST['table']))
    except (KeyError, Food.DoesNotExist):
        return render(request, 'public/index.html', {
            'foods' : foods,
            'categories': categories,
            'tables': tables,
            'error_message': "You didn't select a food."
        })
    else:
        orderd_food.title = selected_food.title
        orderd_food.price = selected_food.price
        orderd_food.category = selected_food.category
        orderd_food.table = selected_table
        orderd_food.time = timezone.now()
        orderd_food.save()
        
        messages.success(request, "You just ordered a food.")
        return HttpResponseRedirect(reverse('public:index'))
    

def serve(request):
    foods = Ordered_food.objects.filter(is_served=False)
    served_foods = Served_food.objects.all()
    served_food = Served_food()
    try:
        selected_food = foods.get(pk=request.POST['food'])
    except (KeyError, Food.DoesNotExist):
        return render(request, 'public/cook.html', {
            'foods' : foods,
            'served_foods' : served_foods,
            'error_message': "You didn't select a food."
        })
    else:
        selected_food.is_served = True
        selected_food.save()
        
        served_food.title = selected_food.title
        served_food.price = selected_food.price
        served_food.category = selected_food.category
        served_food.table = selected_food.table
        served_food.time = timezone.now()
        served_food.save()
        
        messages.success(request, "You just served a food.")
        return HttpResponseRedirect(reverse('public:cook')) 
    
    
def pay(request):
    foods = Served_food.objects.filter(is_paid=False)
    paid_foods = Paid_food.objects.all()
    paid_food = Paid_food()
    try:
        selected_food = foods.get(pk=request.POST['food'])
    except (KeyError, Food.DoesNotExist):
        return render(request, 'public/manager.html', {
            'served_foods' : foods,
            'paid_foods' : paid_foods,
            'error_message': "You didn't select a food."
        })
    else:
        selected_food.is_paid = True
        selected_food.save()
        
        paid_food.title = selected_food.title
        paid_food.price = selected_food.price
        paid_food.category = selected_food.category
        paid_food.table = selected_food.table
        paid_food.time = timezone.now()
        paid_food.save()
        
        messages.success(request, "You just paid for a food.")
        return HttpResponseRedirect(reverse('public:manager')) 
    
