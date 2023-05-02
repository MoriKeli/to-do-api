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

class UpdateTasksView(APIView):
    """
        This view enable a user to update and delete a task. The user will also view details of the selected task.
    """
    
    def get_task(self, taskID):
        """ This method gets a task object from the database using a primary key. """
        try:
            return Tasks.objects.get(id=taskID)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, taskID):
        serializer = TasksSerializer(self.get_task(taskID))
        return Response(serializer.data)
    
    def put(self, request, taskID):
        task = self.get_task(taskID)
        serializer = TasksSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, taskID):
        task = self.get_task(taskID)
        task.delete()
        return Response(
            {"message": "You deleted this task!"},
            status=status.HTTP_204_NO_CONTENT
        )
    