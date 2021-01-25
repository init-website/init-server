from django.contrib import admin
from .models import Project, Homework, Homework_submit
# Register your models here.

admin.site.register(Project)
admin.site.register(Homework)
admin.site.register(Homework_submit)