from django.contrib import admin
from django.urls import path, include
from profiles import urls
from task import urls
from inbox import urls
from user_messages import urls
from task_message import urls
from .views import root_route, logout_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
         'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path('', include('profiles.urls')),
    path('', include('task.urls')),
    path('', include('inbox.urls')),
    path('', include('user_messages.urls')),
    path('', include('task_message.urls')),
    path('', root_route),

]

"""
URL Configuration for the Django project.

This module defines the urlpatterns list, which
includes various paths for different
parts of the application:
- 'admin/' for Django admin site
- 'api-auth/' for Django Rest Framework authentication URLs
- 'dj-rest-auth/logout/' for custom logout route
- 'dj-rest-auth/' for Django Rest Auth URLs
- 'dj-rest-auth/registration/' for Django Rest Auth registration URLs
- Includes paths from 'profiles', 'task', 'inbox', 'user_messages',
  and 'task_message'
  applications using their respective URLs configurations.
- Root route ('') mapped to 'root_route' view function.

Each path is included based on its corresponding application's URLs module.
"""
