from dataclasses import field
from django.contrib import admin

from .models import UserProfile, Account

# Register your models here.



admin.site.register(Account)

class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('email', 'slug',)

admin.site.register(UserProfile, ProfileAdmin)
