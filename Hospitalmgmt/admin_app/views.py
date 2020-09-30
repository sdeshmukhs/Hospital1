from django.shortcuts import render, redirect
from .forms import *
from Hospital.models import Location
from .models import Doctors
from Hospital.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Hospital.models import DoctorsRecruitment
from django.contrib import messages
from rest_framework import viewsets
from . serializers import DoctorSerializer

class DoctorView(viewsets.ModelViewSet):
    query = Doctors.objects.all()
    serializer_class = DoctorSerializer
    
    

@login_required(login_url='login')
def Home1(request):
    return render(request,"admin_home.html")

@login_required(login_url='login')
def Register_doctor(request):
    if request.method == 'POST':
        form = DoctorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home1')
    else:
        form = DoctorsForm()
    return render(request,'register_doctor.html',{'form':form})

@login_required(login_url='login')
def read(request):
    read = Doctors.objects.all()
    return render(request,'doctors_list.html',{'read':read})

@login_required(login_url='login')
def read_appointment(request):
    read = Appointment.objects.all()
    return render(request,'read_appointment.html',{'read':read})

@login_required(login_url='login')
def read_ambulance(request):
    read = Ambulance.objects.all()
    return render(request,'read_ambulance.html',{'read':read})

@login_required(login_url='login')
def read_healthcheckup(request):
    read = HealthCheckup.objects.all()
    return render(request,'read_healthcheckup.html',{'read':read})

@login_required(login_url='login')
def read_criticalcare(request):
    read = CriticalCare.objects.all()
    return render(request,'read_criticalcare.html',{'read':read})


@login_required(login_url='login')
def read_recruitmentcall(request):
    read = DoctorsRecruitment.objects.all()
    return render(request,'read_recruitmentcall.html',{'read':read})



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home1')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register1.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home1')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home1')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def location(request):
    form = LocationForm()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,f'New location added.!')
            return redirect("home")

    else:
        form = LocationForm()

    return render(request, 'location.html',{'form':form})

