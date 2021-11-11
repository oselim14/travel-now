from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django import forms

class Location(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    open_hours = models.TimeField(auto_now=False, auto_now_add=False)
    closing_hours = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('locations_index')
        
class Itinerary(models.Model):
    description = models.TextField(max_length=500, default='')
    city = models.CharField(max_length=100, default='Seattle')
    arrival_date = models.DateField('Arrival Date', default = date.today())
    departure_date = models.DateField('Departure Date', default = date.today())
    locations = models.ManyToManyField(Location)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('detail', kwargs={'itinerary_id': self.id})

class Comment(models.Model):
  date = models.DateField('Posted on', default=date.today())
  content = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for itinerary_id: {self.itinerary_id} @{self.url}"