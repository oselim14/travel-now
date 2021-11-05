from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Itinerary, Location
from .forms import LocationForm
from main_app import models

# Create your views here.

def home(request):
    return HttpResponse('<h1>home</h1>')

def about(request):
    return render(request, 'about.html')

def itinerary_index(request):
    return render(request, 'itinerary/index.html', {'itinerary': itinerary })

def itinerary_detail(request):
    return render(request, 'itinerary/detail.html')

class ItineraryCreate(CreateView):
    model = Itinerary

def add_location(request, itinerary_id, location_id):
    Itinerary.objects.get(id=itinerary_id).locations.add(location_id)
    return redirect('detail', itinerary_id=itinerary_id)

class LocationList(ListView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'

class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations/'   
