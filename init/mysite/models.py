from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

# Create your models here.
class Project(models.Model):
    objects = models.Manager()
    writer = models.CharField(max_length=50)
    #writer = models.ForeignKey('mysite.InitUser', verbose_name = "작성자", on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    #img = models.ImageField(blank=True, null=True, upload_to='') #project_uploads
    img = ProcessedImageField(
        upload_to='project_uploads/', # 저장 위치
        processors=[ResizeToFit(width=600, upscale=False)],
        format='JPEG', # 저장 포맷(확장자)
        options= {'quality': 90 }, # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
    )

    img_thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 60}
    )

    pub_date = models.DateField(auto_now=True)
    contents = models.TextField()
    url = models.TextField(null=True)
    #year = models.DateField(auto_now=True)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Homework(models.Model):
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    writer = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Homework_submit(models.Model):
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE, db_column='homework_id')
    user_id = models.CharField(null=True, max_length=20)
    contents = models.TextField(null=True)
    file = models.FileField(null=True, blank=True, upload_to='homework_uploads/')
    submitted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.homework_id.title

class InitUser(AbstractUser):
    generation = models.CharField(null=False, blank=False, max_length=20)
    git = models.URLField(null=True, blank=True)