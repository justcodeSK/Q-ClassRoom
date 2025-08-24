from django.urls import path
from django import *
from student import views

urlpatterns = [
    path('student',views.student,name="student"),
    path('sy',views.syllabus,name="syllabus"),
    path('pdf',views.pdf,name="pdf"),
    path('vid',views.videos,name="videos"),
    path('vvw',views.vidview,name="vidview"),

  
]


