from django.urls import path   
from profiles import view

urlpatterns = [
    path('/related-tasks/<int:pk>', views.RelatedTasks),
    path('/task-view/<int:pk>', views.TaskView),
    path('/create-task/', views.TaskCreation),
    path('/delete-task/<int:pk>', views.TaskDeletion),
    path('/update-task/<int:pk>', views.TaskUpdate),
]