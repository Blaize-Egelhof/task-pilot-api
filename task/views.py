from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status
from taskpilot.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

class RelatedTasks(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        tasks_owned = Task.objects.filter(owner=user)
        tasks_joined = Task.objects.filter(assigned_users=user)
        tasks = tasks_owned | tasks_joined
        tasks = tasks.distinct() 
        serializer = self.serializer_class(tasks, many=True, context={'request': request})
        return Response(serializer.data)

class TaskView(APIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        is_owner= task.owner ==request.user
        is_member = task.assigned_users.filter(id=request.user.id).exists()
        if is_owner or is_member:
            task = get_object_or_404(Task,pk=pk)
            serializer = self.serializer_class(task)
            return Response(serializer.data)
        else:
            return Response({'error': 'You do not have permission to view this task.'}, status=status.HTTP_403_FORBIDDEN)

class TaskCreation(APIView):
    serializer_class= TaskSerializer
    permission_classes =(IsAuthenticated,)

    def post(self,request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeletion(APIView):
    serializer_class= TaskSerializer
    permission_classes =[IsOwnerOrReadOnly]

    def delete(self, request, pk):
            task = get_object_or_404(Task, pk=pk)
            if request.user == task.owner:
                task.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail': 'You do not have permission to delete this task.'}, status=status.HTTP_403_FORBIDDEN)

class TaskUpdate(APIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] 

    def put(self, request, pk):
        task_to_be_updated = get_object_or_404(Task, pk=pk)
        if request.user == task_to_be_updated.owner:
            serializer = self.serializer_class(task_to_be_updated, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)  
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You do not have permission to update this task.'}, status=status.HTTP_403_FORBIDDEN)




