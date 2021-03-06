from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itinerary/', views.itinerary_index, name='index'),
    path('itinerary/me', views.my_itinerary, name='my_itinerary'),
    path('itinerary/<int:itinerary_id>/', views.itinerary_detail, name='detail'),
    path('itinerary/create/', views.ItineraryCreate.as_view(), name='itinerary_create'),
    path('itinerary/<int:pk>/update/', views.ItineraryUpdate.as_view(), name='itinerary_update'),
    path('itinerary/<int:pk>/delete/', views.ItineraryDelete.as_view(), name='itinerary_delete'),
    path('itinerary/<int:itinerary_id>/add_comment/', views.add_comment, name='add_comment'),
    path('remove_comment/<int:comment_id>/', views.remove_comment, name='remove_comment'),
    path('itinerary/<int:itinerary_id>/add_photo/', views.add_photo, name='add_photo'),
    path('photo/<int:photo_id>/delete/', views.photo_delete, name='photo_delete'),
    path('itinerary/<int:itinerary_id>/add_location/<int:location_id>', views.add_location, name='add_location'),
    path('itinerary/<int:itinerary_id>/remove_location/<int:location_id>', views.remove_location, name='remove_location'),
    path('itinerary/<int:pk>/update_locations/', views.UpdateLocations.as_view(), name='update_locations'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/me/', views.my_locations, name='my_locations'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]