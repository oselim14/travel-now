from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>home</h1>')

def about(request):
    return render(request, 'about.html')

def itinerary_index(request):
    return render(request, 'itinerary/index.html', {'itinerary': itinerary })