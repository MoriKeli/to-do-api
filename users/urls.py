from django.urls import path
from . import views

urlpatterns = [
    path('create-new-task/', views.schedule_task_view, name='new_task'),
    path('task/<str:pk>/', views.edit_tasks_view, name='edit_task'),
]