from rest_framework import serializers
from .models import Task
from task_message.serializers import TaskMessageSerializer

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    task_messages = TaskMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'created_at', 'due_date', 'priority', 'category','state','assigned_users','state_changed_by', 'task_visability' , 'title','is_owner','task_messages'
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    