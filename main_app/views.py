from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Itinerary, Location
from .forms import LocationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def itinerary_index(request):
    itinerary = Itinerary.objects.filter(user=request.user)
    return render(request, 'itinerary/index.html', { 'itinerary': itinerary })

def itinerary_detail(request, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    locations_exclude = Location.objects.exclude(id__in=itinerary.locations.all().values_list('id'))

    return render(request, 'itinerary/detail.html', {
        'itinerary': itinerary,
        'locations': locations_exclude
    })

class ItineraryCreate(CreateView):
    model = Itinerary
    fields = ['city', 'description', 'arrival_date', 'departure_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItineraryUpdate(UpdateView):
    model = Itinerary
    fields = ['description', 'city', 'arrival_date', 'departure_date']

class ItineraryDelete(DeleteView):
    model = Itinerary
    success_url = '/itinerary/'

def add_location(request, itinerary_id, location_id):
    Itinerary.objects.get(id=itinerary_id).locations.add(location_id)
    return redirect('detail', itinerary_id=itinerary_id)

def remove_location(request, itinerary_id, location_id):
    Itinerary.objects.get(id=itinerary_id).locations.remove(location_id)
    return redirect('detail', itinerary_id=itinerary_id)

class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
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


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)