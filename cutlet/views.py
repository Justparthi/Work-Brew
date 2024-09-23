from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm
import smtplib

email = "pywork69@gmail.com"
key = "iuuwhrajukmcezdi"

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gmail = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Print the values to the console (you can change this to logging if needed)
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Message:", message)

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=email, password=key)
        connection.sendmail(from_addr=email, to_addrs="justparthiban@gmail.com", msg=f"Subject:WorkBrew \n\n Mobile:{phone} \n Message:{message}")
        connection.close()
        return render(request, "index.html")

    return render(request, "index.html")  # Assuming your home page template is 'index.html'


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the database
            return redirect('/cafe')  # Redirect to the home page after saving
    else:
        form = PlaceForm()

    return render(request, 'add_place.html', {'form': form})


def place_list(request):
    places = Place.objects.all()  # Query all places from the database
    return render(request, 'place_list.html', {'places': places})


def get(request, id):
    place = get_object_or_404(Place, id=id)
    return render(request, 'place_detail.html', {'place': place})


