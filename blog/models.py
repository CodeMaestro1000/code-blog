from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    url = models.URLField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title[:50]
