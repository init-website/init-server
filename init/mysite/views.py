from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import HomeworkUploadForm, SignupForm
from .models import InitUser, Project, Homework, Homework_submit

def home(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def homework(request):
    user_id = request.user.id
    if user_id:
        user = InitUser.objects.get(id=user_id)
        return redirect('homework_list', user.year)
    return redirect('home')

def homework_list(request, year):
    homeworks = Homework.objects.filter(year=year).order_by('-id')
    user_id = request.user.id
    return render(request, 'homework_list.html', {'homeworks': homeworks, 'user_id': user_id})

def homework_detail(request, year, homework_id):
    homework = Homework.objects.get(id=homework_id)
    return HttpResponse(homework)

def homework_submit(request, year, homework_id):
    homework = Homework.objects.get(id=homework_id)
    user = InitUser.objects.get(id=request.user.id)
    if request.method == "POST":
        form = HomeworkUploadForm(request.POST, request.FILES)

        if  form.is_valid():
            obj = Homework_submit(homework_id=homework, user_id=user, contents=form.data['contents'], file=form.data['file'])
            obj.save()
            return redirect('homework_result', year, homework_id)
    else:
        form = HomeworkUploadForm()
    return render(request, 'homework_submit.html', {
        'form': form, 'homework': homework
    })


def homework_result(requerst, year, homework_id):
    return HttpResponse("homework result page")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate( username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})