from django.shortcuts import render, redirect
from .models import Place
from .forms import PlaceForm


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the database
            return redirect('place_list')  # Redirect to the list of places after saving
    else:
        form = PlaceForm()
    
    return render(request, 'add_place.html', {'form': form})

def place_list(request):
    places = Place.objects.all()  # Query all places from the database
    return render(request, 'place_list.html', {'places': places})



