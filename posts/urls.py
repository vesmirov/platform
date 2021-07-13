from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/new/', views.PostCreateView.as_view(), name='new'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path(
        'posts/<int:pk>/edit/',
        views.PostUpdateView.as_view(),
        name='post_edit'
    ),
    path(
        'posts/<int:pk>/delete/',
        views.PostDeleteView.as_view(),
        name='post_delete'
    ),
    path(
        'posts/<int:pk>/comment/',
        views.PostCommentCreateView.as_view(),
        name='comment_new'
    ),
    path(
        'posts/<int:pk>/comment/<int:comment_pk>/delete/',
        views.PostCommentDeleteView.as_view(),
        name='comment_delete'
    ),
]
