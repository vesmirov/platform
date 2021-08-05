from django.urls import path, include
from rest_framework.authtoken import views as auth_views

from . import views


urlpatterns = [
    path('obtain-auth-token/', auth_views.obtain_auth_token),
    path('v1/notes/', views.NoteListCreate.as_view()),
    path('v1/notes/<int:pk>/', views.NoteRetrieveUpdateDestroy.as_view()),
    path('v1/posts/', views.PostListCreate.as_view()),
    path('v1/posts/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view()),
]
