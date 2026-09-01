from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Reservation
from room.models import Room


# Display all Reservation created of the Client
class ListReservation(ListView):
    models = Reservation
    template_name = ""
    context_object_name = "reservations"


# Show specification a reservation in the Room
class DetailReservation(DetailView):
    models = Reservation
    template_name = ""
    context_object_name = "reservation"


# Create a reservation of a Room in the Hotel
def create_reservation(request):
    if request.method == "POST":

        room = Room()
        form = Reservation(request.POST)

        if form.is_valid:
            client = form.cleaned_data["client"]
            room = form.cleaned_data["room"]
            people = form.cleaned_data["people"]
            enter = form.cleaned_data["enter"]
            exit = form.cleaned_data["exit"]
            payment = form.cleaned_data["payment"]

            if enter == '':
                messages.add(request, messages.INFO, "La fecha de salida no puede quedar vacia")
                return render(request, "")

            elif exit > enter:
                messages.add(request, messages.INFO, "La fecha de salida no debe ser antes que la entrada")
                return render(request, "")

            elif people > room.bedroom:
                messages.add(request, messages.INFO, "El numero de personas supera el maximo que permite la Habitacion")
                return render(request, "")

            elif payment < room.price:
                messages.add(request, messages.INFO, "El pago por la Habitacion a reservar es bajo")
                return render(request, "")

            else:
                reservation = Reservation.objects.create(
                    client = client,
                    room = room,
                    people = people,
                    enter = enter,
                    exit = exit,
                    payment = payment
                )
                messages.add(request, messages.SUCCESS, f"Reserva en la Habitacion {room.number} confirmada")
                return render(request, "", reservation)

        else:
            form = Reservation()
            messages.add(request, messages.INFO, "")
            return render(request, "")


# Client cancel reservation in the Room
def cancel_reservation(request, id):
    if request.method == "POST":

        room = Room.objects.get(pk=id)

        reservation = Reservation.objects.get(pk=id)
        reservation.delete()

        messages.add(request, messages.SUCCESS, f"La reserva en la Habitacion {room.number} se ha Cancelado")
        return render(request, "")