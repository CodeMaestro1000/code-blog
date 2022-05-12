from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView # can also import these along with the ones above, No significant difference for me
from .models import Project, Post
from .forms import ProjectCreateForm, ProjectUpdateForm, PostCreateForm, PostUpdateForm, CommentCreateForm
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

# Mixins should come first before the view you're inheriting from!!!
class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new_project.html'
    model = Project
    form_class = ProjectCreateForm # to add classes to the form for styling

    def form_valid(self, form): # similar to if request.method == POST
        form.instance.author = self.request.user # automatically set author in db to current user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'project_edit.html'
    model = Project
    form_class = ProjectUpdateForm

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'project_detail.html'
    model = Project
    success_url = reverse_lazy('projects')

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

# Post views
class PostListView(ListView):
    template_name = 'posts.html'
    model = Post
    queryset = Post.objects.order_by('-date')
    context_object_name = 'post_list'

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new_post.html'
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form): # similar to if request.method == POST
        form.instance.author = self.request.user # automatically set author in db to current user
        return super().form_valid(form)


class PostDisplay(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs): # view triggered by GET request
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm
        return context

"""
The Django documentation suggests to subclass FormView to get the form handling functionality and combine it with the SingleObjectMixin 
in order to get the post, which will be referenced by the private key as part of the URL."""

# for more, see: https://www.samuelliedtke.com/blog/implement-comment-system-blog-application-django/

class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentCreateForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'

class PostView(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'post_edit.html'
    model = Post
    form_class = PostUpdateForm

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'post_detail.html'
    model = Post
    success_url = reverse_lazy('posts')

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
