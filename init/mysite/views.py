from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Homework

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