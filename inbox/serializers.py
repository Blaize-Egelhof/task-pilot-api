from rest_framework import serializers
from .models import Inbox

class InboxSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Inbox
        if get_is_owner():
            fields = [
                'user','messages','last_updated'
            ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner