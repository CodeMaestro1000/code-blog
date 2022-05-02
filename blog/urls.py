from django.urls import path
from .views import (HomePageView, PostCreateView, ProjectListView, ProjectView, ProjectCreateView, ProjectUpdateView, 
                    ProjectDeleteView, PostListView, PostCreateView, PostView, PostDeleteView, PostUpdateView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project_detail'),
    path('projects/new', ProjectCreateView.as_view(), name='new_project'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='edit_project'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new', PostCreateView.as_view(), name='new_post'),
    path('posts/<int:pk>/', PostView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
    ]