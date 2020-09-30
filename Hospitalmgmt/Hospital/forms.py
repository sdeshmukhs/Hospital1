
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username","password1","password2"]
    username = forms.CharField(widget=forms.TextInput({"placeholder":"Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput({"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput({"placeholder":"Confirm-Password"}))

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = "__all__"

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("Patient_Name","Patient_Age","Reason_of_concern","Patient_Contact","Patient_Address","DATE")
    DATE = forms.DateField(widget=forms.DateInput({"placeholder":"YY/MM/DD"}))

    # def clean_appointment(self,*args,**kwargs):
    #     Patient_Name = self.cleaned_data.get("Patient_Name")
    #     qs = Appointment.objects.filter(Patient_Name__iexact=Patient_Name)
    #     if qs.exists():
    #         raise forms.ValidationError("This name already exists")
    #     return Patient_Name
        


class HealthCheckupForm(forms.ModelForm):
    class Meta:
        model = HealthCheckup
        fields = "__all__"

class CriticalCareForm(forms.ModelForm):
    class Meta:
        model = CriticalCare
        fields = "__all__"


class DoctorsRecruitmentForm(forms.ModelForm):
    class Meta:
        model = DoctorsRecruitment
        fields = "__all__"



