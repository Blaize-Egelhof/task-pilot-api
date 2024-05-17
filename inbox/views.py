from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from taskpilot.permissions import IsOwnerOrReadOnly
from inbox.models import Inbox
from inbox.serializers import InboxSerializer
from messages.models import Message
from messages.serializer import MessageSerializer

class Inbox_View(APIView):
    permission_classes =[IsOwnerOrReadOnly]
    serializer_class = InboxSerializer
    
    def get(self,request):
        inbox = get_object_or_404(Inbox, user=request.user)
        serializer = InboxSerializer(Inbox,context= {'request' : request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        permission_classes = [IsAuthenticated]
        message_to_update = get_object_or_404(Message, pk=pk)

        data = request.data
        if 'accepted' in data:
            message_to_update.accepted = True
            task_to_join = message_to_update.related_task
            task_to_join.assigned_users.add(request.user)
        elif 'declined' in data:
            message_to_update.declined = True
        else:
            return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

        message_to_update.read_status = True
        message_to_update.save()
        
        serializer = MessageSerializer(message_to_update, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
            

        

