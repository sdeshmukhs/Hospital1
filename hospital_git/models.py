from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    specialization = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)

    def __str__(self):
        return self.name


