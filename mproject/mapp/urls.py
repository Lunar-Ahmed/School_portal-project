from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('principal/', views.admin, name='admin'),
    path('bursar/', views.bursar, name='bursar'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('assignment/', views.assignment, name='assignment'),
    path('vice-principal', views.acad, name='acad'),
    
     path('vice-principal/teacher-details/<int:teacher_id>/', views.teacher_details, name='teacher_details'),

    # path('attendance/<int:student_id>/<int:week>/', views.attendance_view, name='attendance_view'),
    path('students/class/<str:class_level>/', views.get_students_by_class, name='get_students_by_class'),
    
    path('vice-principal/teacher_register/', views.teacher_register, name='teacher_register'),
    path('vice-principal/student_register/', views.student_register, name='student_register'),
    
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    # path('teacher/', views.attendance_view, name='attendance_view'),
    
    # path('teacher/<int:teacher_id>/toggle/', views.toggle_teacher_status, name='toggle_teacher_status'),
    

    path('toggle-teacher-status/<int:teacher_id>/', views.toggle_teacher_status, name='toggle_teacher_status'),
    
    
    path('student-scores/', views.student_scores, name='student_scores'),
    path('update-scores/', views.update_scores, name='update_scores'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)