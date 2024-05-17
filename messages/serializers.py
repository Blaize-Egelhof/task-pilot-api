from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'related_task', 'accepted', 'declined', 'title', 'context', 
            'recipient_inbox', 'sender', 'read_status', 'date_created'
        ]