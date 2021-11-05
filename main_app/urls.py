from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itinerary/', views.itinerary_index, name='index'),
    path('itinerary/<int:itinerary_id>/', views.itinerary_detail, name='detail'),
    path('itinerary/create/', views.ItineraryCreate, name='itinerary_create'),
    path('itinerary/<int:itinerary_id>/add_location/', views.add_location, name='add_location'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
   
]