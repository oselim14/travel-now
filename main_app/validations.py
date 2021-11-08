from .models import Itinerary, Location

def itinerary_belongs_to_user(user, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if not itinerary.user.id == user.id:
        return False
    return True

def location_belongs_to_user(user, location_id):
    location = Location.objects.get(id=location_id)
    if not location.user.id == user.id:
        return False
    return True