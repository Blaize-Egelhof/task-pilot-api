from django.urls import path
from . import views

urlpatterns = [
    path('task-messages-send/<int:pk>', views.TaskMessageSend.as_view(), name='task-message-send'),
    path('task-messages-view/<int:pk>', views.TaskMessageView.as_view(), name='task-message-view'),
]