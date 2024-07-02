from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    """
    Serializer for the Profile model, providing fields for serialization
    and readonly access to certain fields like owner's username and
    computed fields like is_owner.

    Fields:
    - id: The unique identifier for the profile.
    - owner: The username of the owner of the profile (readonly).
    - created_at: The datetime when the profile was created.
    - updated_at: The datetime when the profile was last updated.
    - bios: The biography or description associated with the profile.
    - image: The image associated with the profile.
    - public_tasks_count: The number of tasks owned by the profile owner with
      visibility set to 'Public'.
    - joined_tasks_count: The number of tasks where the profile owner is
      assigned with visibility set to 'Public'.
    - is_owner: Boolean indicating whether the current request user is the
      owner of the profile.

    Readonly Fields:
    - id: Readonly field, representing the unique identifier.
    - owner: Readonly field, representing the owner's username.
    - created_at: Readonly field, representing the creation datetime.
    - is_owner: Readonly field, representing whether the current user
      is the owner.

    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'bios', 'image',
            'owned_tasks_count', 'joined_tasks_count', 'is_owner'
        ]
    read_only_fields = ['id', 'owner', 'created_at', 'is_owner']

    """
    Returns a boolean indicating whether the current request user
    is the owner of the profile.
    """

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
