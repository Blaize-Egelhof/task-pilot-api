from django.urls import path
from profiles import views

"""
url endpoint to view,edit,delete profile instances

"""
urlpatterns = [
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
