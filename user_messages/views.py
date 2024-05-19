from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class CreateMessage(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    def post(self,request):
        sender = request.user
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get(self,request):
        user = request.user
        user_related_messages = Message.objects.filter(sender=user)
        serializer = self.serializer_class(user_related_messages,many=True,context={'request': request})
        return Response(serializer.data)

class EditMessage(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    def put(self,request,pk):
        user = request.user
        message_to_update = get_object_or_404(Message,pk=pk)
        serializer = self.serializer_class(message_to_update,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        