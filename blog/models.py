from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=70, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # For all many-to-one relationships we must also specify an on_delete option.
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=300) # short description of project (like a caption of some sort)
    body = models.TextField(blank=False)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)]) # self.id == pk (interchangeable in Django but recommended to use id)
