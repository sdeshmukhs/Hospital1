from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path("home1/",views.Home1,name="home1"),
    path('register1/', views.registerPage, name="register1"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('register/',views.Register_doctor,name='register'),
    path('read/',views.read,name='read'),
    path('read_appointment/',views.read_appointment,name='read_appointment'),
    path('read_amb/',views.read_ambulance,name='read_ambulance'),
    path('read_healthcheckup/',views.read_healthcheckup,name='read_healthcheckup'),
    path('read_criticalcare/',views.read_criticalcare,name='read_criticalcare'),
    path('read_call/',views.read_recruitmentcall,name='read_recruitmentcall'),
    path('location/',views.location, name= 'location'),
]


    

