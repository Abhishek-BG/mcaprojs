from django.urls import path
from . import views
urlpatterns =[
    path("",views.home, name="home"),
    path("login/",views.StudentLogin, name="login"),
    path("dashboard/",views.StudentDashBoard, name="dash")
    #http://127.0.0.1:8000/student/ 
    #https://github.com/Abhishek-BG/mcaprojs
]