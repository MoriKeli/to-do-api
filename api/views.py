from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TasksSerializer
from .models import Tasks

class TasksView(APIView):
    """
        This view enables the user to view all scheduled task in the database and create a new task.
    """
    def get(self, request):
        task = Tasks.objects.all()
        serializer = TasksSerializer(task, many=True)

        return Response(serializer.data)
    

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    