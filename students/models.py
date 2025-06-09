from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)             # CharField
    description = models.TextField()                    # TextField
    is_active = models.BooleanField(default=True)       # BooleanField
    created_at = models.DateTimeField(auto_now_add=True)  # DateTimeField

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)             # CharField
    email = models.EmailField(unique=True)              # EmailField
    age = models.IntegerField()                         # IntegerField
    bio = models.TextField(blank=True)                  # TextField
    is_verified = models.BooleanField(default=False)    # BooleanField
    joined_on = models.DateTimeField(auto_now_add=True) # DateTimeField
    enrolled_courses = models.ManyToManyField(Course)   # ManyToManyField

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)  # OneToOneField
    address = models.TextField()
    phone = models.CharField(max_length=15)
    profile_picture_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Profile of {self.student.name}"

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)       # ForeignKey (Many-to-One)
    title = models.CharField(max_length=100)
    content = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.course.name}"
