from .models import Itinerary, Location, Comment, Photo

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

def photo_belongs_to_user(user, photo_id):
    photo = Photo.objects.get(id=photo_id)
    itinerary = Itinerary.objects.get(id=photo.itinerary.id)
    if not itinerary.user.id == user.id:
        return False
    return True

def comment_belongs_to_user(user, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if not comment.user.id == user.id:
        return False
    return True