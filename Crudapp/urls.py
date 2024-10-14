from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.home_page, name='home_page'),
    path('student-form/', views.student_form, name='student_form'),
    path('read-students/', views.read_stud, name='read_stud'),
    path('save_student/', views.save_student, name='save_student'),  
    path('search_student/', views.search_student, name='search_student'),
    path('update_student/', views.update_student, name='update_student'),
    path('delete_stud_form/', views.delete_student_form, name='delete_stud_form'),
    path('delete/', views.delete, name='delete'),
]
