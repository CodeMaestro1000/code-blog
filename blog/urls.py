from unicodedata import name
from django.urls import path
from .views import HomePageView, ProjectListView, ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project_detail'),
    path('projects/new', ProjectCreateView.as_view(), name='new_project'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='edit_project'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    ]