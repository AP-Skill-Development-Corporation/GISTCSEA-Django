from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):
	return render(request,'bthtml/home.html')

def abt(request):
	return render(request,'bthtml/about.html')

def grid(request):
	return render(request,'bthtml/gdh.html')

def stdr(request):
	return render(request,'bthtml/rg.html')

def stcr(request):
	e = Student.objects.all()
	if request.method=="POST":
		rn = request.POST['r']
		sna = request.POST['s']
		bc = request.POST['b']
		yr = request.POST['y']
		c = Student.objects.create(rln=rn,sn=sna,brch=bc,year=yr)
		return redirect('/')
	return render(request,'bthtml/stdtls.html',{'g':e})

def stup(request,b):
	a = Student.objects.get(id=b)
	if request.method == "POST":
		a.rln = request.POST['r']
		a.sn = request.POST['s']
		a.save()
		return redirect('/')
	return render(request,'bthtml/stupd.html',{'p':a})

