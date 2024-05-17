from django.urls import path
from . import views

urlpatterns = [
    path('task-messages/<int:pk>', views.TaskMessageSend.as_view(), name='task-message-send'),
]