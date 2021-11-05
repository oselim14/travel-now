from django.db import models

# Create your models here.

class Itinerary(models.Model):
    def __str__(self):
        return None


class Location(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    open_hours = models.DateTimeField('Opening Hour')
    closing_hours = models.DateTimeField('Closing Hour')
    address = models.CharField(max_length=250)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name