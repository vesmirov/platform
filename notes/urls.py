from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('notes/', views.NoteListView.as_view(), name='notes'),
    path('notes/new/', views.NoteCreateView.as_view(), name='new'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note'),
    path(
        'notes/<int:pk>/edit/',
        views.NoteUpdateView.as_view(),
        name='note_edit'
    ),
    path(
        'notes/<int:pk>/delete/',
        views.NoteDeleteView.as_view(),
        name='note_delete'
    ),
    path(
        'notes/<int:pk>/comment/',
        views.CommentCreateView.as_view(),
        name='comment_new'
    ),
]
