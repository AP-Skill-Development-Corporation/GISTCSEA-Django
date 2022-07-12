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





