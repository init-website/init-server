from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

# Create your models here.

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

class Project(models.Model):
    objects = models.Manager()
    writer = models.ForeignKey(InitUser, on_delete=models.CASCADE)
    people = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=200, null=False)
    img = ProcessedImageField(
        upload_to='',
        processors=[ResizeToFit(width=960, upscale=False)],
        format='JPEG' 
    )

    img_thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 60}
    )

    pub_date = models.DateField(auto_now=True)
    contents = models.TextField(null=True)
    url = models.URLField(null=True, blank=True)
    #url = models.TextField(null=True)
    #year = models.DateField(auto_now=True)
    year = models.CharField(max_length=4, null=False)

    def __str__(self):
        return self.title
