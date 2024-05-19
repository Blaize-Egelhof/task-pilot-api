from django.urls import path
from . import views

urlpatterns = [
    path('create-message/', views.CreateMessage.as_view(), name='create-message'),
]