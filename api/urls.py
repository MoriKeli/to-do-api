from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksView.as_view(), name='all_tasks'),
    path('update/<str:taskID>/', views.UpdateTasksView.as_view(), name='update_task'),

]