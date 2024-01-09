from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hellow/<str:usrname>', views.hellow),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_tasks/', views.create_task, name='create_tasks'),
    path('create_projects/', views.create_project, name='create_project'),
    path('project_details/<int:id>', views.poject_details, name='project_details'),
]