from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'bios', 'image',
            'public_tasks_count', 'joined_tasks_count', 'is_owner'
        ]
    read_only_fields = ['id', 'owner', 'created_at','is_owner']

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
