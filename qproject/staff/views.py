from django.shortcuts import render,redirect
from staff.models import Staff
from staff.models import Syllabus


# Create your views here.

def staff(request):
    return render(request,'staff.html')

def addsyllabus(request):
     if request.method == 'POST':
            su=request.POST['subject']
            tr=request.POST['teacher']
            da=request.POST['date']
            sy=request.FILES['syllabus']
            x=Syllabus.objects.create(Subject=su,Teacher=tr,Date=da,Syllabus=sy)
            x.save()
            return redirect(staff)
     return render(request,'addsyllabus.html')

def editstaff(request):
    es=Staff.objects.filter(id=request.session['staff_id'])
    return render(request,'editstaff.html',{'da':es})
def staffedit(request,uid):
    se=Staff.objects.get(id=uid)
    return render(request,'formstaff.html',{'da':se})
def updstaff(request,uid):
    if request.method == 'POST':
            nm=request.POST['name']
            ag=request.POST['age']
            pl=request.POST['place']
            em=request.POST['email']
            ph=request.POST['phone']
            ur=request.POST['user']
            ps=request.POST['pass']
            x=Staff.objects.filter(id=uid).update(Name=nm,Age=ag,Place=pl,Email=em,Phone=ph,User=ur,Password=ps)
            return redirect(staff)







