from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from .forms import CreateNewTask, CreateNewProject

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
    return render(request,"projects/projects.html", {
        "projects": projects_list
    })

def tasks(request):
    tasks_list = Tasks.objects.all()
    return render(request,"tasks/tasks.html", {
        "tasks": tasks_list
    })

def create_task(request):
    if request.method == "POST":
        Tasks.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')
    else:
        return render(request,"tasks/create_task.html", {
            'form': CreateNewTask()
        })

def create_project(request):
    if request.method == 'POST':
        Project.objects.create(name=request.POST.get('name'))
        return redirect('projects')
    else:
        return render(request, "projects/create_projects.html", {
            'form': CreateNewProject()
        })

def poject_details(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        "project": project,
        "tasks" : tasks
    })