from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'bthtml/home.html')

def abt(request):
	return render(request,'bthtml/about.html')

def grid(request):
	return render(request,'bthtml/gdh.html')

def stdr(request):
	return render(request,'bthtml/rg.html')