from django.contrib import admin
from django.urls import path,include
from Hospital import views
from admin_app import views
from rest_framework import routers
from admin_app.models import Doctors
from admin_app.views import DoctorView


router = routers.DefaultRouter()
router.register(r'doctors/',DoctorView, basename=Doctors)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/',include('Hospital.urls')),
    path('my_admin/',include('admin_app.urls')),
    path('doctors/',include(router.urls)),


]
