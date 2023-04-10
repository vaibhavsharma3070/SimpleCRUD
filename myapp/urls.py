from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<pk>/', views.UserDetails.as_view()),
]
