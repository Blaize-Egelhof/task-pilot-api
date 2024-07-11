from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Class to check if the requesting user is the owner of object.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
