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
    """
    API view to create and send a new task message associated with a specific
    task.

    Attributes:
    - `serializer_class`: Uses `TaskMessageSerializer` for serializing task
       messages.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `post(request, pk)`: Handles HTTP POST requests to create and send a
      new task message.
    """
    serializer_class = TaskMessageSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        associated_task = get_object_or_404(Task, pk=pk)
        sender = request.user
        is_owner = associated_task.owner == sender

        if is_owner:
            data = {
                'sender': sender.id,
                'associated_task': associated_task.id,
                'context': request.data.get('context', ''),
                'important': request.data.get('important', False)
            }
        else:
            data = {
                'sender': sender.id,
                'associated_task': associated_task.id,
                'context': request.data.get('context', ''),
            }

        serializer = self.serializer_class(
            data=data, context={'request': request}
        )

        if serializer.is_valid():
            task_message = serializer.save()
            associated_task.task_messages.add(task_message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class TaskMessageView(APIView):
    """
    API view to retrieve all task messages associated with a specific task.

    Attributes:
    - `serializer_class`: Uses `TaskMessageSerializer` for serializing
       task messages.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `get(request, pk)`: Handles HTTP GET requests to retrieve all
      task messages.
    """
    serializer_class = TaskMessageSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        associated_task = get_object_or_404(Task, pk=pk)
        task_messages = TaskMessage.objects.filter(
            associated_task=associated_task
        )
        task_serializer = self.serializer_class(
            task_messages, many=True, context={'request': request}
        )
        return Response(task_serializer.data)


class TaskMessageDelete(APIView):
    """
    API view to delete a specific task message.

    Attributes:
    - `serializer_class`: Uses `TaskMessageSerializer` for
       serializing task messages.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `post(request, pk)`: Handles HTTP POST requests to delete a task message.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskMessageSerializer

    def post(self, request, pk):
        try:
            message_to_be_deleted = TaskMessage.objects.get(pk=pk)
        except TaskMessage.DoesNotExist:
            return Response({'error': 'Message not found'},
                            status=status.HTTP_404_NOT_FOUND)

        if (message_to_be_deleted.associated_task.owner == request.user) or (
                message_to_be_deleted.sender == request.user
        ):
            message_to_be_deleted.delete()
            return Response({'success': 'Message has been deleted'},
                            status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'You do not have permission to delete this comment'},
                status=status.HTTP_403_FORBIDDEN,
            )
