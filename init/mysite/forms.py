from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Homework_submit, InitUser
from django.core.exceptions import ValidationError
       
class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'year']
        
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'last_name', 'first_name', 'email', 'year']

class HomeworkUploadForm(forms.ModelForm):
    class Meta:
        model = Homework_submit
        fields = ['contents', 'file']
        widgets = {
            'contents': forms.Textarea(attrs={'class':'form-control mb-3',
          'id': 'exampleFormControlTextarea1',
          'rows': '10'}), 'file': forms.FileInput(attrs={'class': 'form-control-file cl-white', 
          'id': 'exampleFormControlFile1'})
       }