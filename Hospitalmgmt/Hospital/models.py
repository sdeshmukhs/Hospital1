from django.db import models

class Location(models.Model):
    City = models.CharField(max_length=100)
    def __str__(self):
        return self.City



class Ambulance(models.Model):
    Patient_Name = models.CharField(max_length=100)
    Patient_Contact = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Patient_Address = models.CharField(max_length=200)
    DATE = models.DateField()


class Appointment(models.Model):
    Patient_Name = models.CharField(max_length=100, unique=True)
    Patient_Age = models.IntegerField()
    Reason_of_concern = models.CharField(max_length=200)
    Patient_Contact = models.IntegerField()
    Patient_Address = models.CharField(max_length=200)
    DATE = models.DateField()

class HealthCheckup(models.Model):
    Patient_Name = models.CharField(max_length=100)
    Patient_Age = models.IntegerField()
    Reason_of_concern = models.CharField(max_length=200)
    Patient_Contact = models.IntegerField()
    Patient_Address = models.CharField(max_length=200)
    DATE = models.DateField()

class CriticalCare(models.Model):
    Patient_Name = models.CharField(max_length=100)
    Patient_Age = models.IntegerField()
    Reason_of_concern = models.CharField(max_length=200)
    Patient_Contact = models.IntegerField()
    Patient_Address = models.CharField(max_length=200)
    DATE = models.DateField()

class DoctorsRecruitment(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact_Number = models.IntegerField()
    Address = models.CharField(max_length=200)
    Specialization = models.CharField(max_length=50)
    Degree = models.CharField(max_length=50)
    Passout_Year =models.IntegerField()
    Experience = models.IntegerField()


