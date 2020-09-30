from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Ambulance)
admin.site.register(Appointment)
admin.site.register(DoctorsRecruitment)
admin.site.register(CriticalCare)

admin.site.register(Location)
