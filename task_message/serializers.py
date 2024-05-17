from rest_framework import serializers
from .models import TaskMessage

class TaskMessageSerializer(serializers.ModelSerializer):
    message = MessageSerializer()

    class Meta:
        model = TaskMessage
        fields = [
            'sender','associated_task', 'title','context','timestamp'
        ]