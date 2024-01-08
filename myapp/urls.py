from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hellow/<str:usrname>', views.hellow),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
]