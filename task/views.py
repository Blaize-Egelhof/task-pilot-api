from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status
from taskpilot.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer


class RelatedTasks(APIView):

    """
    API view to retrieve tasks related to a specific user requesting.

    Attributes:
    - `permission_classes`: Requires the user to be authenticated.
    - `serializer_class`: Uses `TaskSerializer` for serializing tasks.

    Methods:
    - `get`: Handles HTTP GET requests to fetch tasks owned or joined by the user.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        tasks_owned = Task.objects.filter(owner=user)
        tasks_joined = Task.objects.filter(assigned_users=user)
        tasks = tasks_owned | tasks_joined
        tasks = tasks.distinct()
        serializer = self.serializer_class(tasks, many=True,
                                           context={'request': request})

        return Response(serializer.data)


class TaskView(APIView):
    """
    API view to retrieve details of a specific task.

    Attributes:
    - `serializer_class`: Uses `TaskSerializer` for serializing tasks.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `get`: Handles HTTP GET requests to retrieve details of a task.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        is_owner = task.owner == request.user
        is_member = task.assigned_users.filter(id=request.user.id).exists()
        if is_owner or is_member:
            task = get_object_or_404(Task, pk=pk)
            serializer = self.serializer_class(task,
                                               context={'request': request})
            return Response(serializer.data)
        else:
            return Response({'error':
                            'You do not have permission to view this task.'},
                            status=status.HTTP_403_FORBIDDEN)


class TaskCreation(APIView):
    """
    API view to create a new task.

    Attributes:
    - `serializer_class`: Uses `TaskSerializer` for serializing tasks.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `post`: Handles HTTP POST requests to create a new task.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeletion(APIView):
    """
    API view to delete an existing task.

    Attributes:
    - `serializer_class`: Uses `TaskSerializer` for serializing tasks.
    - `permission_classes`: Uses `IsOwnerOrReadOnly` to check ownership.

    Methods:
    - `delete`: Handles HTTP DELETE requests to delete a task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if request.user == task.owner:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail':
                            'You do not have permission to delete this task.'},
                            status=status.HTTP_403_FORBIDDEN)


class TaskUpdate(APIView):
    """
    API view to update an existing task.

    Attributes:
    - `serializer_class`: Uses `TaskSerializer` for serializing tasks.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `put`: Handles HTTP PUT requests to update a task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        task_to_be_updated = get_object_or_404(Task, pk=pk)
        if request.user == task_to_be_updated.owner:
            serializer = self.serializer_class(task_to_be_updated,
                                               data=request.data,
                                               context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':
                            'You do not have permission to update this task.'},
                            status=status.HTTP_403_FORBIDDEN)


class GrabExcludingUser(APIView):
    """
    API view to fetch all users excluding those assigned to a specific task.

    Attributes:
    - `serializer_class`: Uses `UserSerializer` for serializing users.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `get`: Handles HTTP GET requests to fetch users not assigned to the task.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        assigned_user_ids = task.assigned_users.values_list('id', flat=True)
        users = User.objects.exclude(id__in=assigned_user_ids)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)


class LeaveTask(APIView):
    """
    API view to allow a user to leave a task.

    Attributes:
    - `serializer_class`: Uses `TaskSerializer` for serializing tasks.
    - `permission_classes`: Requires the user to be authenticated.

    Methods:
    - `put`: Handles HTTP PUT requests to remove a user from a task.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        user_requesting = request.user

        if user_requesting in task.assigned_users.all():
            task.assigned_users.remove(user_requesting)
            task.save()
            serializer = self.serializer_class(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'error': (
                        'Could not leave the task. '
                        'Are you sure you are a member of this task?'
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )
