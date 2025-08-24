from django.shortcuts import render,redirect
from teacher.models import Teacher
from teacher.models import Videos
from student.models import Student
from staff.models import Staff


# Create your views here.
def teacher(request):
     if request.method == 'POST':
            su=request.POST['subject']
            tr=request.POST['teacher']
            da=request.POST['date']
            vi=request.FILES['video']
            x=Videos.objects.create(Subject=su,Teacher=tr,Date=da,Videos=vi)
            x.save()
     return render(request,'teacher.html')


def editstud(request):
    es=Student.objects.all()
    return render(request,'editstud.html',{'da':es})
def studedit(request,uid):
    se=Student.objects.get(id=uid)
    return render(request,'formstud.html',{'da':se})
def updstd(request,uid):
    if request.method == 'POST':
            nm=request.POST['name']
            ag=request.POST['age']
            pl=request.POST['place']
            em=request.POST['email']
            ph=request.POST['phone']
            ur=request.POST['user']
            ps=request.POST['pass']
            x=Student.objects.filter(id=uid).update(Name=nm,Age=ag,Place=pl,Email=em,Phone=ph,User=ur,Password=ps)
            return redirect(teacher)

def editteach(request):
    et=Teacher.objects.filter(id=request.session['teach_id'])
    return render(request,'editteach.html',{'da':et})
def teachedit(request,uid):
    te=Teacher.objects.get(id=uid)
    return render(request,'formteach.html',{'da':te})
def updteach(request,uid):
    if request.method == 'POST':
            nm=request.POST['name']
            ag=request.POST['age']
            pl=request.POST['place']
            em=request.POST['email']
            ph=request.POST['phone']
            ur=request.POST['user']
            ps=request.POST['pass']
            x=Teacher.objects.filter(id=uid).update(Name=nm,Age=ag,Place=pl,Email=em,Phone=ph,User=ur,Password=ps)
            return redirect(teacher)

def staffview(request):
    sv=Staff.objects.all()
    return render(request,'staffview.html',{'da':sv})





