from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


"""
Serializer for customizing the UserDetailsSerializer to
include additional profile information.

Attributes:
- profile_id (ReadOnlyField):
  Read-only field that retrieves the ID of the associated profile.
- profile_image (ReadOnlyField):
  Read-only field that retrieves the URL of the profile image.

Meta:
- Inherits fields from UserDetailsSerializer.Meta.fields
  and adds 'profile_id' and 'profile_image'.
"""


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
