from rest_framework import serializers
from .models import TaskMessage

class TaskMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskMessage
        fields = [
            'sender','associated_task', 'title','context','timestamp'
        ]