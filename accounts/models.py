from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser, models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_info', args=[str(self.id)])