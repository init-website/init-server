from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Homework_submit, InitUser

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
       
class SignupForm(UserCreationForm):
    class Meta:
        model = InitUser
        fields = ['username','email','first_name','last_name','year','git']
