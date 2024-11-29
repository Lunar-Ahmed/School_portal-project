from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('principal/', views.admin, name='admin'),
    path('bursar/', views.bursar, name='bursar'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('assignment/', views.assignment, name='assignment'),
    path('vice-principal', views.acad, name='acad'),
    path('vice-principal/teacher_register/', views.teacher_register, name='teacher_register'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    ]