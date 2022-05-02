from django.forms import ModelForm
from .models import Project, Post, Comment

class ProjectCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs) # overwrite default properties of certain fields
        self.fields['title'].widget.attrs = { 'class': 'form-input' }
        self.fields['description'].widget.attrs = { 'class': 'form-input', 'id': 'description-field' }
        self.fields['body'].widget.attrs = { 'class': 'form-input', 'id': 'body-field' }

    class Meta:
        model = Project
        fields = ['title', 'description', 'body']

class ProjectUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = { 'class': 'form-input' }
        self.fields['description'].widget.attrs = { 'class': 'form-input', 'id': 'description-field' }
        self.fields['body'].widget.attrs = { 'class': 'form-input', 'id': 'body-field' }

    class Meta:
        model = Project
        fields = ['title', 'description', 'body']


class PostCreateForm(ModelForm):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['title'].widget.attrs = { 'class': 'form-input' }
        self.fields['body'].widget.attrs = { 'class': 'form-input', 'id': 'body-field' }

    class Meta:
        model = Post
        fields = ['title', 'body']


class PostUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = { 'class': 'form-input' }
        self.fields['body'].widget.attrs = { 'class': 'form-input', 'id': 'body-field' }

    class Meta:
        model = Project
        fields = ['title', 'body']


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']
    
    def __init__(self,  *args, **kwargs):
        # Save the request with the form so it can be accessed in clean_*()
        # self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs = { 'class': 'form-input' }
        self.fields['comment'].widget.attrs = { 'class': 'form-input', 'id': 'comment-field' }
        
