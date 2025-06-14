from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/edit/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    #urls of course
    path('course/',views.read_all_course,name="read_all_course"),
    path('create_course/',views.create_course,name="create_course"),
    path('course/<int:cl>/',views.create_details,name="create_details"),
    path('course/edit/<int:id>/',views.edit_course,name="edit_course"),
     path('course/delete/<int:id>/',views.delete_course,name="delete_course"),
    #api urls
     path('api', views.fetchAPi, name='student_list'),
]
