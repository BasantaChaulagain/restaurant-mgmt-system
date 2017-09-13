from django.contrib import admin
from .models import Table, Constant, Category, Food, Ordered_food, Served_food, Paid_food

    
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ['price']
    search_fields = ['title']
    
class OrderedFoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'table', 'time', 'is_served')
    list_filter = ['time']
    search_fields = ['title']

class ServedFoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'table', 'time', 'is_paid')
    list_filter = ['time']
    search_fields = ['title']

class PaidFoodAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'category', 'price', 'table', 'time')
    list_filter = ['time']
  
class ConstantAdmin(admin.ModelAdmin):
    list_display = ('serviceCharge', 'vat')
    
        
admin.site.register(Food, FoodAdmin)
admin.site.register(Ordered_food, OrderedFoodAdmin)
admin.site.register(Served_food, ServedFoodAdmin)
admin.site.register(Paid_food, PaidFoodAdmin)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(Constant, ConstantAdmin)