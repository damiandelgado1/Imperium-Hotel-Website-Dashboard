from django.shortcuts import render
from room.models import Room


# Main page of the Hotel
def main_page(request):
    room = Room.objects.all()
    return render(request, "home/base.html", {"rooms": room})


# Restaurant of the Hotel
def restaurant(request):
    return render(request, "home/restaurant.html")


# Information of the Hotel
def about_us(request):
    return render(request, "home/about_us.html")

