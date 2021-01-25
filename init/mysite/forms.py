from django import forms
from .models import Homework_submit

class HomeworkUploadForm(forms.ModelForm):
    class Meta:
        model = Homework_submit
        fields = ['contents', 'file']