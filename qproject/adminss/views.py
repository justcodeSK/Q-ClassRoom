from django.shortcuts import render,redirect
from teacher.models import Teacher
from teacher.models import Videos
from student.models import Student
from staff.models import Staff
from staff.models import Syllabus

# Create your views here.
def admins(request):
    return render(request,'admins.html')

def teachapr(request):
    ta=Teacher.objects.filter(Value=0)
    return render(request,'teachapr.html',{'da':ta})
def teachaproved(request,uid):
    ta=Teacher.objects.get(id=uid)
    ta.Value=1
    ta.save()
    return redirect(admins)

def studapr(request):
    sa=Student.objects.filter(Value=0)
    return render(request,'studapr.html',{'da':sa})
def studaproved(request,uid):
    ta=Student.objects.get(id=uid)
    ta.Value=1
    ta.save()
    return redirect(admins)

def staffapr(request):
    sa=Staff.objects.filter(Value=0)
    return render(request,'staffapr.html',{'da':sa})
def staffaproved(request,uid):
    ta=Staff.objects.get(id=uid)
    ta.Value=1
    ta.save()
    return redirect(admins)

def deleteteach(request):
    dt=Teacher.objects.all()
    return render(request,'deleteteach.html',{'da':dt})
def delteach(request,uid):
    td=Teacher.objects.get(id=uid)
    td.delete()
    return redirect(admins)

def deletestud(request):
    ds=Student.objects.all()
    return render(request,'deletestud.html',{'da':ds})
def delstud(request,uid):
    ts=Student.objects.get(id=uid)
    ts.delete()
    return redirect(admins)

def deletevid(request):
    dv=Videos.objects.all()
    return render(request,'deletevid.html',{'da':dv})
def delvid(request,uid):
    dv=Videos.objects.get(id=uid)
    dv.delete()
    return redirect(admins)

def deletesyl(request):
    dv=Syllabus.objects.all()
    return render(request,'deletesyl.html',{'da':dv})
def delsyl(request,uid):
    dv=Syllabus.objects.get(id=uid)
    dv.delete()
    return redirect(admins)

