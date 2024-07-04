from django.urls import path
from . import views

"""
URL patterns for task message-related views.

These patterns map specific endpoints to corresponding view
classes for handling sending, viewing, and deleting task messages.


Endpoints:
- 'task-messages-send/<int:pk>': Maps
   to TaskMessageSend view for sending task messages.
- 'task-messages-view/<int:pk>':
   Maps to TaskMessageView view for viewing task messages.
- 'task-message-delete/':
   Maps to TaskMessageDelete view for deleting
   task messages.
"""

urlpatterns = [
    path('task-messages-send/<int:pk>', views.TaskMessageSend.as_view(),
         name='task-message-send'),
    path('task-messages-view/<int:pk>', views.TaskMessageView.as_view(),
         name='task-message-view'),
    path('task-messages-delete/<int:pk>', views.TaskMessageDelete.as_view(),
         name='task-message-view'),
]
