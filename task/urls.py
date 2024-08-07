from django.urls import path
from . import views

"""
URL patterns for task management endpoints.

Defines URL routes to handle various operations related to tasks,
including creation, deletion, updating,viewing tasks and leaving tasks.
Also includes endpoints for fetching related tasks and retrieving
all users.
"""

urlpatterns = [
    path('related-tasks/<int:pk>', views.RelatedTasks.as_view(),
         name='related-tasks'),
    path('task-view/<int:pk>', views.TaskView.as_view(),
         name='task-view'),
    path('create-task/', views.TaskCreation.as_view(),
         name='create-task'),
    path('delete-task/<int:pk>', views.TaskDeletion.as_view(),
         name='delete-task'),
    path('update-task/<int:pk>', views.TaskUpdate.as_view(),
         name='update-task'),
    path('users/<int:pk>', views.GrabExcludingUser.as_view(),
         name='all-users'),
    path('leave-task/<int:pk>', views.LeaveTask.as_view(),
         name='all-users'),
]
