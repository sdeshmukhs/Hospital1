from django.contrib import admin
from . models import Doctors

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','specialization']

admin.site.register(Doctors)


