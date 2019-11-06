from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Work aavunond")

def login(request):
	return render(request,'pages/login.html')	

def workerreg(request):
	return render(request,'pages/workerreg.html')

def cusreg(request):
	return render(request,'pages/cusreg.html')	

def trial(request):
	return render(request,'pages/trial.html')	

def new(request):
	return render(request,'pages/new.html')		

def aa(request):
	return render(request,'pages/aa.html')		

def l(request):
	return render(request,'pages/l.html')	

def addskill(request):
	return render(request,'pages/addskill.html')	

def reg(request):
	return render(request,'pages/reg.html')

def home(request):
	return render(request,'pages/home.html')