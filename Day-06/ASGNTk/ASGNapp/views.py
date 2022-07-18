from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def reg(request):
	if request.method == "POST":
		w = Usreg(request.POST)
		if w.is_valid():
			w.save()
			messages.success(request,'Successfully Created a record')
			return redirect('/lgn')
	w = Usreg()
	return render(request,'html/register.html',{'a':w})