from django.contrib import admin
from .models import UserProfile, Tasks

@admin.register(UserProfile)
class UserProfileTable(admin.ModelAdmin):
    list_display = ['name', 'gender', 'country', 'phone_no']
    readonly_fields = []