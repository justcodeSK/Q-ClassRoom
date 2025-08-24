from django.shortcuts import render
from teacher.models import Teacher
from teacher.models import Videos
from staff.models import Syllabus


# Create your views here.
def student(request):
    st=Teacher.objects.all()
    return render(request,'student.html',{'da':st})

def videos(request):
    vi=Videos.objects.all()
    return render(request,'videos.html',{'da':vi})
def vidview(request):
    vi=Videos.objects.all()
    return render(request,'vidview.html',{'da':vi})

def syllabus(request):
    sy=Syllabus.objects.all()
    return render(request,'syllabus.html',{'da':sy})
def pdf(request):
    sy=Syllabus.objects.all()
    return render(request,'pdf.html',{'da':sy})

