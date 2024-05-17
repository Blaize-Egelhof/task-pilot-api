from django.urls import path
from . import views

urlpatterns = [
    path('task-messages/<int:pk>', views.MessageSend.as_view(), name='task-message-send'),
]