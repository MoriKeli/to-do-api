from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class TasksTable(admin.ModelAdmin):
    list_display = ['task', 'subtitle', 'created']