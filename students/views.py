from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request): #controller 
    return HttpResponse("<h1>Welcome to Students Home Page</h1>")

def StudentLogin(request):
    return HttpResponse(" <h1>Login Page</h1>")

def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")