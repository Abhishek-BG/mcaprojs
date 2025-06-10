from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request): #controller 
    return render(request,'students/home.html')

def StudentLogin(request):
    return render(request,'students/login.html')
    #return render(request,templatefile name)

def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")
