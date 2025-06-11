from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Student
from .forms import StudentForm
pages= [{'name':'Home Page','url':'home'},
        {'name':'Login Page','url':'login'}
]
#create 
def student_create(req):
    if req.method=="POST":
        form = StudentForm(req.POST) #object mapping
        if form.is_valid(): #
            form.save() # saved to DB
            return redirect('home') #home page
    else:
        form = StudentForm()
    return render(req,'students/student_create.html',
                    {'form':form}
                    )




#read all
def home(request): #controller  #http://127.0.0.1:8000/students/
    #all the students details 
    students = Student.objects.all();
    return render(request,'students/home.html',
                  context={'students':students,
                           'items':pages})
def StudentLogin(request):
    return HttpResponse(" <h1>Login</h1>")

    print(request)
    return response
def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")
