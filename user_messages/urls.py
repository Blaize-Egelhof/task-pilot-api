from django.urls import path
from . import views

urlpatterns = [
    path('create-message/', views.CreateMessage.as_view(),
         name='create-message'),
    path('message-list/', views.MessageList.as_view(),
         name='message-list'),
    path('edit-message/<int:pk>', views.EditMessage.as_view(),
         name='edit-message')
]
