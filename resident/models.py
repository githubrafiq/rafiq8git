from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic')

    success_url = '/'

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
