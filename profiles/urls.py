from django.urls import path
from profiles import views

"""
url endpoint to view,edit,delete profile instances based on the type
of request made (get,put,post etc)

"""
urlpatterns = [
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
