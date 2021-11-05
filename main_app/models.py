from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.



class Location(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    open_hours = models.DateTimeField('Opening Hour')
    closing_hours = models.DateTimeField('Closing Hour')
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('locations_index')
        
        
class Itinerary(models.Model):
    locations = models.ManyToManyField(Location)
    def __str__(self):
        return None

    def get_absolute_url(self):
        return reverse('itinerary_detail', kwargs={'itinerary_id': self.id})