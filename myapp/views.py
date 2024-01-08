from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks

# Create your views here.
def index(request):
    title = "Welcome to Django Course"
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    usrname = "Omar"
    return render(request, 'about.html', {
        'usrname' : usrname
    })

def hellow(request, usrname):
    print(usrname)
    return HttpResponse("<h1>Hellow %s<h1>" % usrname)

def projects(request):
    #projects_list = list(Project.objects.values())
    projects_list = Project.objects.all()
    return render(request,"projects.html", {
        "projects": projects_list
    })

def tasks(request):
    tasks_list = Tasks.objects.all()
    return render(request,"tasks.html", {
        "tasks": tasks_list
    })