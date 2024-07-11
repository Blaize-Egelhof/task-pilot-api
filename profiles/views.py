from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from rest_framework import status
from taskpilot.permissions import IsOwnerOrReadOnly


class ProfileDetail(APIView):
    """
    API endpoint for retrieving, updating,
    or deleting a specific profile instance.

    Attributes:
    - permission_classes: Controls access permissions
      using IsOwnerOrReadOnly to allow owners full access
      and others read-only access.
    - serializer_class: Serializer used for converting profile
      instances to and from JSON format.

    Methods:
    - get_object: Retrieves a profile instance based on the
      provided primary key (pk) and checks permissions.
    - get: Retrieves and serializes details of a specific
      profile instance.
    - put: Updates a specific profile instance with new
      data from the request payload.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data,
                                       partial=True,
                                       context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)
