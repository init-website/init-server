from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InitUser

class UserForm(UserCreationForm):
    class Meta:
        model = InitUser
        fields = ['username','email','first_name','last_name','generation','git']