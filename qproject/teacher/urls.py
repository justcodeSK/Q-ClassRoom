from django.urls import path
from django import *
from teacher import views


urlpatterns = [
    path('teacher',views.teacher,name="teacher"),

    path('estud',views.editstud,name="editstud"),
    path('stude/<int:uid>',views.studedit,name="studedit"),
    path('upds/<int:uid>',views.updstd,name="updstd"),

    path('eteach',views.editteach,name="editteach"),
    path('teache/<int:uid>',views.teachedit,name="teachedit"),
    path('updt/<int:uid>',views.updteach,name="updteach"),

    path('sv',views.staffview,name="staffview"),
    
  
]


