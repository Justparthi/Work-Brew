from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'map_url', 'img_url', 'location', 'has_sockets', 'has_toilet', 'has_wifi', 'can_take_calls', 'seats', 'coffee_price', 'stable_wifi', 'power_sockets', 'quiet', 'calls', 'tables', 'coffee', 'food', 'veggie', 'payment', 'restroom']


