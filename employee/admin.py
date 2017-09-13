from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile, attend, salary


#userprofile extension
class profileinline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"


class CustomUserAdmin(UserAdmin):
    inlines = (profileinline,)

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)


#attendance table on admin site
class attendAdmin(admin.ModelAdmin):
    list_display = ('a_user','a_date','a_time')
    list_filter =  ['a_date']
    search_fields = ['a_user']

admin.site.register(attend, attendAdmin)


#salary table on admin site
class salaryAdmin(admin.ModelAdmin):
    list_display = ('s_user','s_paiddate','s_paidtime')
    list_filter =  ['s_user']
    search_fields = ['a_user']

admin.site.register(salary, salaryAdmin)