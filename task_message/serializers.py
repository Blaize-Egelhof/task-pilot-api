from rest_framework import serializers
from .models import TaskMessage


class TaskMessageSerializer(serializers.ModelSerializer):

    is_owner = serializers.SerializerMethodField()
    sender_profile = serializers.CharField(source='sender.profile.picture_url', read_only=True)

    class Meta:
        model = TaskMessage
        fields = [
            'sender', 'associated_task', 'title', 'context', 'timestamp','is_owner','sender_profile'
        ]


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner