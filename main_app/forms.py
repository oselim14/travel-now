from django.forms import ModelForm
from .models import Comment, Itinerary

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class LocationsForm(ModelForm):
    class Meta:
        model = Itinerary
        fields = ['locations']
