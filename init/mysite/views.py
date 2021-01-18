from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all() #queryset
    return render(request, 'home.html', {'projects': projects})

def new(request):
 
    return render(request, 'new.html')