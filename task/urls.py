from django.urls import path
from . import views

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
]
