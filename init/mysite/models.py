from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

# Create your models here.

class InitUser(AbstractUser):
    student_number = models.CharField(max_length=10, null=False, blank=False)
    year = models.CharField(max_length=20, null=False, blank=False)
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to='profile/')
    birthday = models.DateField(null=True, blank=True)
    git = models.URLField(max_length=60, null=True, blank=True)


class Homework(models.Model):
    year = models.CharField(max_length=20, blank=False)
    title = models.CharField(max_length=200, blank=False)
    contents = models.TextField(blank=False)
    writer = models.ForeignKey(InitUser, on_delete=models.DO_NOTHING, db_column='writer')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=False)

    def __str__(self):
        return self.title

class Homework_submit(models.Model):
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE, db_column='homework_id')
    user_id = models.ForeignKey(InitUser, on_delete=models.CASCADE, db_column='user_id')
    contents = models.TextField(blank=False)
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
    year = models.CharField(max_length=4, null=False)

    def __str__(self):
        return self.title
