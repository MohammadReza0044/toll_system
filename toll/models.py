from django.db import models
from mapbox_location_field.models import LocationField 


class Owner(models.Model):
    name = models.CharField(max_length=200)
    national_code = models.IntegerField()
    age = models.IntegerField()
    total_toll_paid = models.IntegerField(default=0)
   

class Car(models.Model):
    small = "SMALL"
    big = "BIG"

    TYPE_CHOICES = (
        (small, "SMALL"),
        (big, "BIG"),
    )

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    color = models.CharField(max_length=200)
    lenght = models.DecimalField(max_digits=3, decimal_places=2)
    load_valume = models.DecimalField(null=True, max_digits=4, decimal_places=1)
    ownerCar = models.ForeignKey(Owner, on_delete=models.CASCADE)







class Road(models.Model):
    name = models.CharField(max_length=255)
    width = models.DecimalField(max_digits=16, decimal_places=15)
    geom = models.CharField(max_length=255) 



class TollStaion(models.Model):
    name = models.CharField(max_length=200)
    toll_per_cross = models.IntegerField()
    location = LocationField()  



