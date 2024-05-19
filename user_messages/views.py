from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status

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
       

