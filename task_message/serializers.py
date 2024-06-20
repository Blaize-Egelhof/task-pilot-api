from rest_framework import serializers
from .models import TaskMessage
from profiles.models import Profile

class TaskMessageSerializer(serializers.ModelSerializer):
    sender_profile_image_url = serializers.SerializerMethodField()
    is_owner =serializers.SerializerMethodField()
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = TaskMessage
        fields = [
            'id','sender', 'associated_task', 'title', 'context', 'timestamp', 'sender_profile_image_url','is_owner','sender_username'
        ]

    def get_sender_username(self, obj):
        sender = obj.sender
        try:
            profile = Profile.objects.get(owner=sender)
            return profile.owner.username  
        except Profile.DoesNotExist:
            return 'Unknown'  


    def get_sender_profile_image_url(self, obj):
        sender = obj.sender
        try:
            profile = sender.profile
            if profile and profile.image:
                return profile.image.url
            return 'Error getting profile URL'
        except Profile.DoesNotExist:
            return 'Error getting profile URL'  

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user:
            return request.user == obj.associated_task.owner
        return False
