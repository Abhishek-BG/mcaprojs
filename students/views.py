# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Course
from .forms import StudentForm,CourseForm
from django.http import HttpResponse
# CREATE STUDENT
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# READ (List View) STUDENT
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# READ (Detail View) STUDENT
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

# UPDATE STUDENT
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student) #get
    return render(request, 'students/student_form.html',
                   {'form': form})

# DELETE STUDENT
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

#  COURSE READ ALL /course
def read_all_course(request):
    course = Course.objects.all()
    return render(request,'students/courses.html',context={'courses':course})

#  CREATE course /create-course
def create_course(request):
    if request.method=='POST':
         form = CourseForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('/student')
    else:       
        form = CourseForm()
    return render(request,'students/create_course.html',
                  context={'form':form})

#READ COURSE Individual 
def create_details(request,cl):
    course_object = get_object_or_404(Course,pk=cl)
    return render(request,'students/course_details.html',
                  context={'course':course_object})

#edit course 
def edit_course(request,id):


    course_object = get_object_or_404(Course,pk=id)
    if request.method=='POST':
        form = CourseForm(request.POST,instance=course_object)
        if form.is_valid():
            form.save()
            return redirect('/student/course')
    else:
        form = CourseForm(instance=course_object)
        return render(request,'students/create_course.html',
                  context={'form':form})
    
def delete_course(request,id):
    course_object = get_object_or_404(Course,pk=id)
    course_object.delete()
    return HttpResponse("<h1>Course Deleted</h1>")