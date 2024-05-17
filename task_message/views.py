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
    permission_classes =(IsAuthenticated,)
    def post(self,request,pk):
        serializer = self.serializer_class(TaskMessage,context={'request': request})
        associated_task = get_object_or_404(Task, pk=pk)
        if request.user in associated_task.assigned_users.all():
            if serializer.is_valid():
                serializer.save(sender=request.user,associated_task=associated_task,)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You do not have permission to add a comment to this task.'}, status=status.HTTP_403_FORBIDDEN)
