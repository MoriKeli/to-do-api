from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TasksSerializer
from .models import Tasks

@api_view(['GET', 'POST'])
def schedule_task_view(request):
    if request.method == 'GET':
        scheduled_task = get_object_or_404(Tasks)
        serializer = TasksSerializer(scheduled_task)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
