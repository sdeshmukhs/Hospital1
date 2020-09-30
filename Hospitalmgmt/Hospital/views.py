
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import *
from .models import *
from django.contrib import messages

def Home(request):
    return render(request,"home.html")


def about(request):
    return render(request,"about.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,f'Account Created.!')
            # return redirect('join')

    else:
        form = SignUpForm()
    return render(request, "signup.html",{"form":form})

def join(request):
    return render(request,'join.html')

def services(request):
    return render(request,'services.html')

def ambulance(request):
    if request.method == "POST":
        form = AmbulanceForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,f'Ambulance request sent.!')
            return redirect('ambulance_success')

    else:
        form = AmbulanceForm()
    return render(request,'ambulance.html',{'form':form})

def ambulance_success(request):
    return render(request, 'ambulance_success.html')

def See_Ambulance_Request(request):
    see_ambulance = Ambulance.objects.all()
    return render(request,"see_ambulance.html",{"see_ambulance":see_ambulance})

def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            
            form.save()
            messages.success(request,f'Appointment Request Sent.!')
            return redirect('home')

    else:
        form = AppointmentForm()
    return render(request,'appointment.html', {'form':form})

def Healthcheckup(request):
    if request.method == "POST":
        form = HealthCheckupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Request sent.!')
            return redirect('home')

    else:
        form = HealthCheckupForm()
    return render(request,'healthcheckup.html', {'form':form})


def Criticalcare(request):
    if request.method == "POST":
        form = CriticalCareForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Request sent.!')
            return redirect('home')

    else:
        form = CriticalCareForm()
    return render(request,'criticalcare.html', {'form':form})

def recruitment_doctor(request):
    if request.method == 'POST':
        form = DoctorsRecruitmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your Application Submited.!')
            return redirect('r_success')
    else:
        form = DoctorsRecruitmentForm()
    return render(request,'recruitment_doctor.html',{'form':form})



def recruitment_success(request):
        return render(request,'recruitment_success.html')



def Read_Location(request):
    read = Location.objects.all()
    return render(request,"read_location.html",{"read":read})
