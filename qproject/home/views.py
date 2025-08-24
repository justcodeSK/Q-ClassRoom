from django.shortcuts import render,redirect
from django import *
from teacher.models import Teacher
from student.models import Student
from staff.models import Staff
from django.contrib.auth import authenticate,login,logout
from adminss.views import admins
from student.views import student
from teacher.views import teacher
from staff.views import staff

# Create your views here.

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
            nm=request.POST['name']
            ag=request.POST['age']
            pl=request.POST['place']
            em=request.POST['email']
            ty=request.POST['utype']
            ph=request.POST['phone']
            ur=request.POST['user']
            ps=request.POST['pass']
            if ty == "Teacher":
                x=Teacher.objects.create(Name=nm,Age=ag,Place=pl,Email=em,Type=ty,Phone=ph,User=ur,Password=ps)
                x.save()
                return redirect(home) 
            elif ty == "Student":
                x=Student.objects.create(Name=nm,Age=ag,Place=pl,Email=em,Type=ty,Phone=ph,User=ur,Password=ps)
                x.save()
                return redirect(home)
            elif ty == "Staff":
                x=Staff.objects.create(Name=nm,Age=ag,Place=pl,Email=em,Type=ty,Phone=ph,User=ur,Password=ps)
                x.save()
                return redirect(home)

    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        USERNAME=request.POST['username']
        PASSWORD=request.POST['pass']
        users=authenticate(username=USERNAME,password=PASSWORD)
        if users is not None and users.is_superuser == 1:
            return redirect(admins)
        if Student.objects.filter(User=USERNAME,Password=PASSWORD).exists():
            sts=Student.objects.filter(User=USERNAME,Password=PASSWORD)
            for i in sts:
                if i.Value==1:
                    request.session['stud_id']=i.id
                    return redirect(student)
                else:
                    return redirect(login)
        if Teacher.objects.filter(User=USERNAME,Password=PASSWORD).exists():
            tea=Teacher.objects.filter(User=USERNAME,Password=PASSWORD)
            for i in tea:
                if i.Value==1:
                    request.session['teach_id']=i.id
                    return redirect(teacher)
        if Staff.objects.filter(User=USERNAME,Password=PASSWORD).exists():
            sta=Staff.objects.filter(User=USERNAME,Password=PASSWORD)
            for i in sta:
                if i.Value==1:
                    request.session['staff_id']=i.id
                    return redirect(staff)
        else:
            return render(request,'alert.html')

    else:
        return render(request,'login.html')

def logout(request):
    return redirect(home)