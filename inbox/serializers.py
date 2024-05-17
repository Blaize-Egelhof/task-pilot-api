from rest_framework import serializers
from messages.serializers import MessageSerializer
from .models import Inbox

class InboxSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Inbox
        fields = ['user', 'messages', 'last_updated']