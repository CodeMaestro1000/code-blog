from django.forms import ModelForm
from .models import Project

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