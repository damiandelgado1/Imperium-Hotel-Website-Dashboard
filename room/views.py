from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Room


# Display all Room availability in the Hotel
class ListRoom(ListView):
    model = Room
    template_name = ""
    context_object_name = "rooms"


# Show specification of the a Room in the Hotel
class DetailRoom(DetailView):
    model = Room
    template_name = ""
    context_object_name = "room"


# Manage all Room in the Hotel
class ManageRoom(ListView):
    model = Room
    template_name = ""
    context_object_name = "rooms"


# Edit state a Room in the Hotel
class EditRoom(DetailRoom):
    model = Room
    template_name = ""
    context_object_name = "room"


# Create new Room in the Hotel to reservation
class CreateRoom(CreateView):
    model = Room
    fields = [
        "number",
        "preview",
        "description",
        "bedroom",
        "bathroom",
        "availability",
        "price"
    ]
    template_name = ""
    success_url = reverse_lazy("")


# Modify state a Room in the Hotel
class ModifyRoom(UpdateView):
    model = Room
    fields = [
        "availability",
        "price"
    ]
    template_name = ""
    success_url = reverse_lazy("")


# Delete Room in the Hotel
class DeleteRoom(DeleteView):
    model = Room
    template_name = ""
    success_url = reverse_lazy("")