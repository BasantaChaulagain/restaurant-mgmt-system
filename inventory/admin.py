from django.contrib import admin

from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'qtt', 'rate', 'price')
    list_filter = ['price']
    search_fields = ['title']

admin.site.register(Stock, StockAdmin)