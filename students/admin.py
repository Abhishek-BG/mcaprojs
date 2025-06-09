from django.contrib import admin
from .models import Student, Course, StudentProfile, Assignment

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False

class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentProfileInline]
    list_display = ('name', 'email', 'age', 'is_verified', 'joined_on')
    list_filter = ('is_verified',)
    search_fields = ('name', 'email')
    ordering = ('-joined_on',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date')
    list_filter = ('course', 'due_date')
    search_fields = ('title', 'course__name')

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StudentProfile)
admin.site.register(Assignment, AssignmentAdmin)
