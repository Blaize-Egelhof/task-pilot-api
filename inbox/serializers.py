from rest_framework import serializers
from user_messages.serializers import MessageSerializer
from .models import Inbox
from user_messages.models import Message

class InboxSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Inbox
        fields = ['user', 'messages', 'last_updated']

    def get_messages(self, obj):
        messages = Message.objects.filter(recipient_inbox=obj)
        return MessageSerializer(messages, many=True).data