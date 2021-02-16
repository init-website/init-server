from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import HomeworkUploadForm, CreateUserForm, UpdateUserForm
from .models import InitUser, Profile, Project, Homework, Homework_submit
import datetime

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('/login')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def update(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
	    form = UpdateUserForm(instance = user)
    return render(request, 'update.html', {'form': form})

def profile(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def homework(request):
    user = request.user
    if user.is_authenticated:
        user = InitUser.objects.get(username=user.username)
        return redirect('homework_list', user.year)
    return redirect('home')

def homework_list(request, year):
    homeworks = Homework.objects.filter(year=year).order_by('-id')
    user_id = request.user.id
    done = True
    return render(request, 'homework_list.html', {'homeworks': homeworks, 'done' : done})

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

def projects(request):
    if request.method == "POST":
        if request.POST['generation']:
            gen = request.POST['generation']
            postlist = Project.objects.filter(year=gen).order_by('-id')
    else:
        gen = "2020"
        postlist = Project.objects.all().order_by('-id')
    return render(request, 'projects.html', {'postlist':postlist, 'gen':gen})

def project_detail(request, pk):
    post = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'post':post})

def project_new(request):
    if request.method == 'POST':
        new_article=Project.objects.create(
            title=request.POST['postname'],
            writer = request.user,
            people = request.POST['people'],
            contents=request.POST['contents'],
            img=request.FILES['img'],
            pub_date=datetime.datetime.now(),
            url=request.POST['url'],
            year= request.POST['year'],
        )
        # print("User: " + str(request.user))

        return redirect('/projects/')
    return render(request, 'project_new.html')
   
def project_delete(request, pk):
    post = Project.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/projects/')
    return render(request, 'project_delete.html', {'post': post})

def project_update(request, post_id):
    post = Project.objects.get(id=post_id)
    if request.user != post.writer:
        messages.warning(request, "권한 없음")
        return redirect('/projects/')

    if request.method == "POST":
        post.title = request.POST['postname']
        post.people = request.POST['people']
        post.contents = request.POST['contents']
        post.img = request.FILES['img'] #수정 필요
        post.url=request.POST['url']
        post.save()
        return redirect('/projects/' + str(post.id))

    else:
        return render(request, 'project_update.html', {'post':post})  


