from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import HomeworkUploadForm, UserForm
from .models import Project, Homework, Homework_submit
import datetime

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

def projects(request):
    postlist = Project.objects.all().order_by('-id')
    return render(request, 'projects.html', {'postlist':postlist})

def project_detail(request, pk):
    post = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'post':post})

def project_new(request):
    if request.method == 'POST':
        if request.POST['img']:
            new_article=Project.objects.create(
                title=request.POST['postname'],
                contents=request.POST['contents'],
                img=request.POST['img'],
                pub_date=datetime.datetime.now(),
                url=request.POST['url'],
                year= datetime.datetime.now().year,
            )
        else:
            new_article=Project.objects.create(
                title=request.POST['postname'],
                contents=request.POST['contents'],
                img=request.POST['img'],
                pub_date=datetime.datetime.now(),
                url=request.POST['url'],
                year= datetime.datetime.now().year,
            )
        return redirect('/projects/')
    return render(request, 'project_new.html')

def project_delete(request, pk):
    post = Project.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/projects/')
    return render(request, 'project_delete.html', {'Post': post})

def project_update(request, post_id):
    post = Project.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST['postname']
        post.contents = request.POST['contents']
        post.img = request.POST['img']
        post.url=request.POST['url']
        post.save()
        return redirect('/projects/' + str(post.id))

    else:
        return render(request, 'project_update.html')   