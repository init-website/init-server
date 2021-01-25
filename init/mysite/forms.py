from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Homework_submit

class HomeworkUploadForm(forms.ModelForm):
    class Meta:
        model = Homework_submit
        fields = ['contents', 'file']

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")
