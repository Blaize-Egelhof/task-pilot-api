from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class DefaultGreeting(APIView):

    def get(self,request):
        return Response({'Welcome! To My Task Pilot API'})
