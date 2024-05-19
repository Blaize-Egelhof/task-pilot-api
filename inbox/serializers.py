from rest_framework import serializers
from user_messages.serializers import MessageSerializer
from .models import Inbox
from user_messages.models import Message

class InboxSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Inbox
        fields = ['user', 'messages', 'last_updated','is_owner']

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user