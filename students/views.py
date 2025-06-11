from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Student


pages= [{'name':'Home Page','url':'home'},
        {'name':'Login Page','url':'login'}
]
def home(request): #controller  #http://127.0.0.1:8000/students/
    #all the students details 
    students = Student.objects.all();
    return render(request,'students/home.html',
                  context={'students':students,
                           'items':pages})
def StudentLogin(request):
    return render(request,'students/login.html'
                  ,context={'items':pages})
    #return render(request,templatefile name)

def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")
