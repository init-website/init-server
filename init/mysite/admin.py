from django.contrib import admin
from .models import Project, Homework, InitUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Project)
admin.site.register(Homework)
admin.site.register(InitUser)