from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('v1/notes/', views.NoteAPIView.as_view()),
    path('v1/notes/<int:pk>/', views.NoteDetailAPIView.as_view()),
]
