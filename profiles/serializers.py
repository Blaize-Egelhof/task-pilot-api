from rest_framework import serializers
from .models import Profile
from task.models import Task
from django.contrib.auth.models import User
from django.db.models import Q


class ProfileSerializer(serializers.ModelSerializer):

    """
    Serializer for Profile model.
    Includes additional fields and methods to serialize Profile data,
    calculate task counts, and determine ownership status.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owned_tasks_count = serializers.SerializerMethodField()
    joined_tasks_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'bios', 'image',
            'owned_tasks_count', 'joined_tasks_count', 'is_owner'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'is_owner']

    def get_is_owner(self, obj):
        """Determines if the current user is the owner of the profile."""
        request = self.context.get('request')
        return request.user == obj.owner

    def get_owned_tasks_count(self, obj):
        """
        Returns the count of tasks owned by the user.
        """
        owner_id = obj.owner.id
        return Task.objects.filter(owner=owner_id).count()

    def get_joined_tasks_count(self, obj):
        """
        Returns the count of tasks where the user is assigned.
        """
        owner_id = obj.owner.id
        return Task.objects.filter(
            assigned_users=owner_id,
        ).count()
