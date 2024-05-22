from django.contrib import admin
from django.urls import path,include
from profiles import urls
from task import urls
from inbox import urls
from user_messages import urls
from task_message import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('profiles.urls')),
    path('', include('task.urls')),
    path('', include('inbox.urls')),
    path('', include('user_messages.urls')),
    path('', include('task_message.urls')),

]
