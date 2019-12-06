from django.db import models
from beautyapp.models import Services

# Create your models here.



class Addstaff(models.Model):
    name = models.CharField(max_length=250)
    mobileno=models.CharField(max_length=12)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Guest(models.Model):
    gname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)
    treatment_by = models.ForeignKey(Addstaff, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.CharField(max_length=50)
    time_in = models.TimeField()
    time_out = models.TimeField()
    total_time = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    payment  =models.CharField(max_length=100)
    comments = models.CharField(max_length=500,default="NA")

    def __str__(self):
        return self.gname
