from django.db import models

# Create your models here.

class Student(models.Model):
	b = [
		('DN',"Select Your Branch"),
		('CSE','Computer Science and Engineering'),
		('MECH','Mechanical Engineering'),
	]
	y = [
		(0,'Select Your Year'),
		(1,'1st Year'),
		(2,'2nd Year'),
		(3,'3rd Year'),
		(4,'4th Year'),
	]
	rln = models.CharField(max_length=11)
	sn = models.CharField(max_length=150)
	brch = models.CharField(choices=b,default='DN',max_length=5)
	year = models.IntegerField(choices=y,default=0)
