from django.urls import path
from .views import HomePageView, ProjectPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectPageView.as_view(), name='projects'),
    ]