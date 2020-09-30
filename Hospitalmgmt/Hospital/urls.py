from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("home/",views.Home,name="home"),
    path('signup/',views.signup,name='signup'),
    path("accounts/",include("django.contrib.auth.urls")),
    path('about/',views.about, name='about'),
    path('join/', views.join, name= 'join'),
    path('services/',views.services,name='services'),
    path('ambulance/',views.ambulance,name='ambulance'),
    path('appointment/',views.appointment,name='appointment'),
    path('success/',views.ambulance_success,name='ambulance_success'),
    path('healthcheckup/',views.Healthcheckup,name='healthcheckup'),
    path('criticalcare/',views.Criticalcare,name='criticalcare'),
    path('doctors_recruitment/',views.recruitment_doctor,name='recruitment'),
    path('recruitment_success/',views.recruitment_success,name='r_success'),
    
    path("See_Ambulance_Request/",views.See_Ambulance_Request,name="See_Ambulance_Request"),

]