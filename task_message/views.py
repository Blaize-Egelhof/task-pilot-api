from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TaskMessage
from task.models import Task
from .serializers import TaskMessageSerializer
from django.http import Http404
from rest_framework import status
from taskpilot.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

class TaskMessageSend(APIView):
    serializer_class = TaskMessageSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        associated_task = get_object_or_404(Task, pk=pk)
        
        if (request.user in associated_task.assigned_users.all()) or (request.user == associated_task.owner):
            serializer = self.serializer_class(data=request.data, context={'request': request})
            
            if serializer.is_valid():
                task_message = serializer.save(sender=request.user, associated_task=associated_task)
                associated_task.task_messages.add(task_message)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You do not have permission to add a comment to this task.'}, status=status.HTTP_403_FORBIDDEN)

        
class TaskMessageView(APIView):
    serializer_class = TaskMessageSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        associated_task = get_object_or_404(Task, pk=pk)
        task_messages = TaskMessage.objects.filter(associated_task=associated_task)
        task_serializer = self.serializer_class(task_messages, many=True, context={'request': request})
        return Response(task_serializer.data)
