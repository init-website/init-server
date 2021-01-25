from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HomeworkUploadForm
from .models import Project, Homework, Homework_submit

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
    if request.method == "POST":
        form = HomeworkUploadForm(request.POST, request.FILES)

        if  form.is_valid():
            instance = Homework.objects.get(id=homework_id)
            obj = Homework_submit(homework_id=instance, contents=form.data['contents'], file=form.data['file'])
            obj.save()
            return redirect('result', year, homework_id)
    else:
        form = HomeworkUploadForm()
    return render(request, 'submit.html', {
        'form': form
    })


def homework_result(requerst, year, homework_id):
    return HttpResponse("homework result page")