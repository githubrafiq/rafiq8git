from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile_pic')
