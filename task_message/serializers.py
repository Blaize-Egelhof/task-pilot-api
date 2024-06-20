from rest_framework import serializers
from .models import TaskMessage

class TaskMessageSerializer(serializers.ModelSerializer):
    # sender_profile = serializers.CharField(source='sender.profile.picture_url', read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = TaskMessage
        fields = [
            'sender', 'associated_task', 'title', 'context', 'timestamp', 'is_owner',
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user:
            return request.user == obj.sender or request.user == obj.associated_task.owner
        return False
