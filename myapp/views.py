from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellow(request):
    return HttpResponse("<h1>Hellow World!<h1>")

def about(request):
    return HttpResponse("About")