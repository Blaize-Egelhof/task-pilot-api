from rest_framework import serializers
from .models import Task
from task_message.serializers import TaskMessageSerializer
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for converting Task model instances to and from JSON format.

    Attributes:
    - owner (ReadOnlyField): Username of the owner of the task.
    - is_owner (SerializerMethodField):
      Indicates if the current user is the owner of the task.
    - task_messages (TaskMessageSerializer):
      Serializer for task messages associated with the task.
    - assigned_users (PrimaryKeyRelatedField):
      Primary keys of users assigned to the task.

    Methods:
    - get_is_owner: Retrieves whether the current user is the owner of the task.
    - update:Updates a task instance with validated data,
      including managing assigned users.

    Note:
    - 'assigned_users' can be set to None,
      allowing tasks to have no assigned users.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    task_messages = TaskMessageSerializer(many=True, read_only=True)
    assigned_users = serializers.PrimaryKeyRelatedField(
           queryset=User.objects.all(), many=True, required=False)
    assigned_usernames = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'created_at', 'due_date', 'priority', 'category',
            'state', 'assigned_users', 'state_changed_by', 'task_visability',
            'title', 'is_owner', 'task_messages', 'description','assigned_usernames',
        ]

    """
    Checks if the current user is the owner of the task.

    Returns:
    - bool: True if the current user matches the task's owner, False otherwise.
    """

    def get_assigned_usernames(self, obj):
        assigned_users = obj.assigned_users.all()
        return UserSerializer(assigned_users, many=True).data

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

        """
        Updates a task instance with validated data,
        including managing assigned users.

        Returns:
        - Task: Updated task instance.
        """

    def update(self, instance, validated_data):
        assigned_users = validated_data.pop('assigned_users', None)
        instance = super().update(instance, validated_data)

        if assigned_users is not None:
            instance.assigned_users.set(assigned_users)

        return instance

    """
    Serializer for converting User model instances to and from JSON format.

    Attributes:
    - id (IntegerField): The unique identifier for the user.
    - username (CharField): The username of the user.
    """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
