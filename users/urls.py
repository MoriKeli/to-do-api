from django.urls import path
from . import views

urlpatterns = [
    path('create-new-task/', views.schedule_task_view, name='new_task'),
    
]