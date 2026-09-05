from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Menu_Item


# Display all Item of the Menu Restaurant
class ListMenuItem(ListView):
    model = Menu_Item
    template_name = "restaurant/list_menu_item.html"
    context_object_name = "menu_items"


# Show information of the Item in Restaurant
class DetailMenuItem(DetailView):
    model = Menu_Item
    template_name = "restaurant/detail_menu_item.html"
    context_object_name = "menu_item"


# Create a new Item in the Menu Restaurant
class CreateMenuItem(CreateView):
    model = Menu_Item
    fields = [
        "name",
        "stock",
        "price"
    ]
    template_name = "restaurant/create_menu_item.html"
    success_url = reverse_lazy("restaurant")


# Modify a Item in the Menu Restaurant
class ModifyMenuItem(UpdateView):
    model = Menu_Item
    fields = [
        "stock",
        "price"
    ]
    template_name = "restaurant/modify_menu_item.html"
    success_url = reverse_lazy("restaurant")


# Delete a Item of the Menu Restaurant
class DeleteMenuItem(DeleteView):
    model = Menu_Item
    template_name = "restaurant/delete_menu_item.html"
    success_url = reverse_lazy("restaurant")