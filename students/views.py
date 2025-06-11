from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Student

people = [
    {'name':'raju','age':20,'active':True,'per':98},
    {'name':'chotta bheem','age':29,'active':True,'per':93},
    {'name':'mukesh','age':22,'active':False,'per':96},
    {'name':'kirmada','age':20,'active':True,'per':90},
    ]
def home(request): #controller  #http://127.0.0.1:8000/students/
    return render(request,'students/home.html',
                  context={'peoples':people})


def StudentLogin(request):
    return render(request,'students/login.html')
    #return render(request,templatefile name)

def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")
