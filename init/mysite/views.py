from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Project, Homework
from .forms import UserForm

# Create your views here.

def home(request):
    projects = Project.objects.all() #queryset
    return render(request, 'home.html', {'projects': projects})

def new(request):
    return render(request, 'new.html')

def homework(request, year):
    homeworks = Homework.objects.filter(year=year).order_by('-id')
    return render(request, 'homework.html', {'homeworks': homeworks})

def homework_detail(request, year, homework_id):
    return HttpResponse("homework detail page")

def homework_submit(request, year, homework_id):
    return HttpResponse("homework submit page")

def homework_result(requerst, year, homework_id):
    return HttpResponse("homework result page")

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})