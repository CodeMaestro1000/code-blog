from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # For all many-to-one relationships we must also specify an on_delete option.
    date = models.DateField(default=timezone.now())
    description = models.TextField(max_length=300) # short description of project (like a caption of some sort)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)]) # self.id == pk (interchangeable in Django but recommended to use id)
