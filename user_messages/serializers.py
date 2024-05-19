from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'related_task', 'accepted', 'declined', 'title', 'context', 
            'recipient_inbox', 'sender', 'read_status', 'date_created', 'is_owner'
        ]
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.sender