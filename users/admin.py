from django.contrib import admin
from .models import UserProfile, Tasks

@admin.register(UserProfile)
class UserProfileTable(admin.ModelAdmin):
    list_display = ['name', 'gender', 'country', 'phone_no']
    

@admin.register(Tasks)
class TasksTable(admin.ModelAdmin):
    list_display = ['task', 'subtitle', 'created']