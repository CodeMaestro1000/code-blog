from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ProjectPageView(ListView):
    template_name = 'projects.html'
    model = Project
    queryset = Project.objects.order_by('-date')
    context_object_name = 'project_lists'
