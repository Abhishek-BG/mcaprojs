from django.db import models
# http://127.0.0.1:8000/admin
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Assignment(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)
    #Many to One
    title = models.CharField(max_length=100)
    content = models.TextField()
    due_date = models.DateTimeField()
    def __str__(self):
        return f"{self.title} - {self.course.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    bio= models.TextField(blank=True) 
    is_verified= models.BooleanField(default=False)
    joined_on = models.DateTimeField(auto_now_add=True)
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.name}: Verified:{self.is_verified}"
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student,
                                   on_delete=models.CASCADE)
    phone= models.IntegerField()
    addr = models.TextField(blank=True)
    profile_url = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.student.name}'s Profile"