from django import forms
from .models import Student,Course,Assignment
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
    