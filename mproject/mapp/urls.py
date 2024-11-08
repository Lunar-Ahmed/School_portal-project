from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admins/', views.admin, name='admin'),
    path('bursar/', views.bursar, name='bursar'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('assignment/', views.assignment, name='assignment'),
     
    path('authority_register/', views.authority_register, name='authority_register'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('student_register/', views.student_register, name='student_register'),
    path('student_login/', views.student_login, name='student_login'),
    # path('admin_login/admins', views.user_register, name='user_register'),
    path('enroll_form', views.enroll_form, name='enroll_form')
]