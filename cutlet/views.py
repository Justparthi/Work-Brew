from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm


def home(request):
    return render(request, "index.html")  # Assuming your home page template is 'index.html'


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the database
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = PlaceForm()

    return render(request, 'add_place.html', {'form': form})


def place_list(request):
    places = Place.objects.all()  # Query all places from the database
    return render(request, 'place_list.html', {'places': places})


def get(request, id):
    place = get_object_or_404(Place, id=id)
    return render(request, 'place_detail.html', {'place': place})