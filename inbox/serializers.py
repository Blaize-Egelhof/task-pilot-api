from rest_framework import serializers
from .models import Inbox
from messages.serializers import MessageSerializer

class InboxSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Inbox
        fields = ['user', 'messages', 'last_updated']