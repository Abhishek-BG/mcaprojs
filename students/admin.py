from django.contrib import admin

from .models import Course,Assignment,Student,StudentProfile
# Register your models here.

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Student)
admin.site.register(StudentProfile)

#steps to create super admin
# command -> python manage.py createsuperuser