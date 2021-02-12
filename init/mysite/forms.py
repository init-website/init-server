from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Homework_submit, InitUser
from django.core.exceptions import ValidationError

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
       
class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)
    class Meta:
        model = InitUser
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'student_number', 'year']
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = InitUser.objects.filter(username=username)
        if r.count():
            raise  ValidationError("이 아이디는 이미 사용중입니다.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = InitUser.objects.filter(email=email)
        if r.count():
            raise  ValidationError("이미 존재하는 이메일입니다.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("비밀번호가 동일하지 않습니다.")

        return password2

    def save(self, commit=True):
        user =  InitUser.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user