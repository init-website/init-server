from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class InitUser(AbstractUser):
    year = models.CharField(default="2020",max_length=20, null=False, blank=False)
    git = models.URLField(default="git" , null=True, blank=True)

class Homework(models.Model):
    year = models.CharField(default="2020",max_length=20, null=False, blank=False)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    writer = models.ForeignKey(InitUser, on_delete=models.CASCADE, db_column='writer')
    created_at  = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Homework_submit(models.Model):
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE, db_column='homework_id')
    user_id = models.ForeignKey(InitUser, on_delete=models.CASCADE, db_column='user_id')
    contents = models.TextField(null=True)
    file = models.FileField(null=True, blank=True, upload_to='homework_uploads/')
    submitted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.homework_id.title 