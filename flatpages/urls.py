from django.urls import path

from . import views


urlpatterns = [
    path('author/', views.AuthorPage.as_view(), name='author'),
    path('tech/', views.TechPage.as_view(), name='tech'),
]
