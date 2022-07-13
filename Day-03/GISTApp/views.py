from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dsmsg(request):
	return HttpResponse("Welcome to APSSDC Program")

def eve(request):
	return HttpResponse("hello good evening to")

def stdtls(request,n):
	return HttpResponse("Hello User {}".format(n))

def empd(rt,na,eid):
	return HttpResponse("Employee Name: {}<br/> Employee Id: {}".format(na,eid))

def gh(rg,name):
	return HttpResponse("<h3>Good Morning User <span style='color:green'>{}</span></h3>".format(name))

def ed(t,en,eid,age):
	return HttpResponse("<html><head><title>Employee Details</title><body><h3>Employee Name: <span style='color:red'>{}</span></h3><br/><h4>Employee Id: <span style='color:green'>{}</span></h4><br/><h5>Employee Age: <span style='color:blue'>{}</span></h5></body></head></html>".format(en,eid,age))

def hk(t):
	return HttpResponse("<html><head><title>Demo</title><style>h4{color:red}</style></head><body><h4>Hello</h4></body></html>")

def hkm(rt):
	return HttpResponse("<script>alert('Hi user Ramesh')</script>")

def gm(rt,na):
	return HttpResponse("<script>alert('Hi user {}')</script>".format(na))

def k(y):
	return render(y,'ht/demo.html')

def stf(k,er):
	return render(k,'ft.html',{'name':er})

def dt(q,n,ag):
	context = {'name':n,'age':ag}
	return render(q,'ht/v.html',context)

def reg(request):
	return render(request,'ht/register.html')


