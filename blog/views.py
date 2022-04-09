from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # can also import these along with the ones above, No significant difference for me
from .models import Project
from .forms import ProjectCreateForm, ProjectUpdateForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ProjectListView(ListView):
    template_name = 'projects.html'
    model = Project
    queryset = Project.objects.order_by('-date')
    context_object_name = 'project_lists'


class ProjectView(DetailView): # individual project view
    template_name = 'project_detail.html'
    model = Project
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    template_name = 'new_project.html'
    model = Project
    form_class = ProjectCreateForm # to add classes to the form for styling

class ProjectUpdateView(UpdateView):
    template_name = 'project_edit.html'
    model = Project
    form_class = ProjectUpdateForm

class ProjectDeleteView(DeleteView):
    template_name = 'project_detail.html'
    model = Project
    success_url = reverse_lazy('projects')
