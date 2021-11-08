from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
import os
from .models import Itinerary, Location, Comment, Photo
from .forms import CommentForm

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
    comment_form = CommentForm()

    return render(request, 'itinerary/detail.html', {
        'itinerary': itinerary,
        'locations': locations_exclude,
        'comment_form': comment_form
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

def add_comment(request, itinerary_id):
  form = CommentForm(request.POST)

  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.user = request.user
    new_comment.itinerary = Itinerary.objects.get(id=itinerary_id)
    new_comment.save()
  return redirect('detail', itinerary_id=itinerary_id)

def remove_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    itinerary_id = comment.itinerary.id
    comment.delete()
    return redirect('detail', itinerary_id=itinerary_id)

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

def add_photo(request, itinerary_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, itinerary_id = itinerary_id)
        except:
            print('An error occurred uploading file to s3')
    return redirect('detail', itinerary_id=itinerary_id)

def photo_delete(request, photo_id):
    photo = Photo.objects.get(id = photo_id)
    itinerary_id = photo.itinerary.id
    photo.delete()
    return redirect('detail', itinerary_id=itinerary_id)
    

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

