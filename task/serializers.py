from rest_framework import serializers
from .models import Task
from task_message.serializers import TaskMessageSerializer
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    task_messages = TaskMessageSerializer(many=True, read_only=True)
    assigned_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'created_at', 'due_date', 'priority', 'category',
            'state', 'assigned_users', 'state_changed_by', 'task_visability',
            'title', 'is_owner', 'task_messages','description',
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def update(self, instance, validated_data):
        assigned_users = validated_data.pop('assigned_users', None)
        instance = super().update(instance, validated_data)

        if assigned_users is not None:
            instance.assigned_users.set(assigned_users)

        return instance