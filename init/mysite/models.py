from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Project(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Homework(models.Model):
    objects = models.Manager()
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    writer = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title