from django.urls import path
from django import *
from staff import views

urlpatterns = [
    path('staff',views.staff,name="staff"),
    path('as',views.addsyllabus,name="addsyllabus"),
    path('es',views.editstaff,name="editstaff"),
    path('stfe/<int:uid>',views.staffedit,name="staffedit"),
    path('updstf/<int:uid>',views.updstaff,name="updstaff"),
    

]

