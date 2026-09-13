from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Room


# Display all Room availability in the Hotel
class ListRoom(ListView):
    model = Room
    template_name = "room/list_room.html"
    context_object_name = "rooms"


# Show specification of the a Room in the Hotel
class DetailRoom(DetailView):
    model = Room
    template_name = "room/detail_room.html"
    context_object_name = "room"


# Manage all Room in the Hotel
class ManageRoom(ListView):
    model = Room
    template_name = "dashboard_room/manage_room.html"
    context_object_name = "rooms"


# Edit state a Room in the Hotel
class EditRoom(DetailRoom):
    model = Room
    template_name = "dashboard_room/edit_room.html"
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
    template_name = "dashboard_room/create_room.html"
    success_url = reverse_lazy("home")


# Modify state a Room in the Hotel
class ModifyRoom(UpdateView):
    model = Room
    fields = [
        "availability",
        "price"
    ]
    template_name = "dashboard_room/modify_room.html"
    success_url = reverse_lazy("home")


# Delete Room in the Hotel
class DeleteRoom(DeleteView):
    model = Room
    template_name = "dashboard_room/delete_room.html"
    success_url = reverse_lazy("home")