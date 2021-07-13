from django.urls import path

from . import views


app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes'),
    path('new/', views.NoteCreateView.as_view(), name='new'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note'),
    path(
        '<int:pk>/edit/',
        views.NoteUpdateView.as_view(),
        name='note_edit'
    ),
    path(
        '<int:pk>/delete/',
        views.NoteDeleteView.as_view(),
        name='note_delete'
    ),
    path(
        '<int:pk>/comment/',
        views.NoteCommentCreateView.as_view(),
        name='comment_new'
    ),
    path(
        '<int:pk>/comment/<int:comment_pk>/delete/',
        views.NoteCommentDeleteView.as_view(),
        name='comment_delete'
    ),
]
