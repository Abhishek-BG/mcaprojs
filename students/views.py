from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Students Home Page</h1>")
