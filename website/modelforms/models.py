from django.db import models
 # Create your models here.
from django.urls import reverse
from django.core.validators import MaxLengthValidator

 
RADIO_CHOICES = [['1','Petrol'],['2','Diesel']] 
class Car(models.Model):
 
    car_name = models.CharField(max_length=100)
    car_price = models.BigIntegerField()
    car_horsepower = models.IntegerField()
    car_mileage = models.TextField()
    car_brand = models.CharField(max_length=100)
    CHOICES = (('petrol', 'petrol'), ('diesel', 'diesel'))
    car_fueltype = models.CharField(max_length=10, choices=CHOICES)
    select = (('Automatic', 'Automatic'), ('Manual', 'Manual'))
    car_geartype =  models.CharField(("Selected your choice"),max_length=10,choices=select)
   
   # car_geartype = models.CharField(required = True, choice = select, widget=models.RadioSelect(attrs={'class' : 'Radio'}), initial=1)
    # on submit click on the entry page, it redirects to the url below. 
    def get_absolute_url(self):
        return reverse('modelforms:index')
