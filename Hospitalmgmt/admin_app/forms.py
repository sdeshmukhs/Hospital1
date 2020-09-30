from django import forms
from . models import *
from Hospital.models import Location
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = "__all__"



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
        

