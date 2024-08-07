from rest_framework.decorators import api_view
from rest_framework.response import Response

from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    """
    Endpoint for the root of the TaskPilot API.

    Returns a simple JSON response with a welcome message.
    """
    return Response({
        "message": "Welcome to my TaskPilot API!"
    })


@api_view(['POST'])
def logout_route(request):
    """
    Endpoint to log out a user and clear authentication cookies.

    Clears JWT authentication and refresh cookies from the client's browser.
    """
    response = Response(
        {'message': 'Logged out successfully! Cookies cleared.'},
        status=200
    )
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
