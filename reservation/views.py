from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Reservation
from room.models import Room


# Display all Reservation created of the Client
class ListReservation(ListView):
    model = Reservation
    template_name = "reservation/list_reservation.html"
    context_object_name = "reservations"


# Show specification a reservation in the Room
class DetailReservation(DetailView):
    model = Reservation
    template_name = "reservation/detail_reservation.html"
    context_object_name = "reservation"


# Create a reservation of a Room in the Hotel
@login_required
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
                messages.add_message(request, messages.INFO, "La fecha de salida no puede quedar vacia")
                return render(request, "reservation/create_reservation.html")

            elif exit > enter:
                messages.add_message(request, messages.INFO, "La fecha de salida no debe ser antes que la entrada")
                return render(request, "reservation/create_reservation.html")

            elif people > room.bedroom:
                messages.add_message(request, messages.INFO, "El numero de personas supera el maximo que permite la Habitacion")
                return render(request, "reservation/create_reservation.html")

            elif payment < room.price:
                messages.add_message(request, messages.INFO, "El pago por la Habitacion a reservar es bajo")
                return render(request, "reservation/create_reservation.html")

            else:
                reservation = Reservation.objects.create(
                    client = client,
                    room = room,
                    people = people,
                    enter = enter,
                    exit = exit,
                    payment = payment
                )
                messages.add_message(request, messages.SUCCESS, f"Reserva en la Habitacion {room.number} confirmada")
                return render(request, "reservation/create_reservation.html", {"reservation": reservation})

        else:
            form = Reservation()
            messages.add_message(request, messages.INFO, "Ingrese correctamente los datos para realizar la Reserva")
            return render(request, "reservation/create_reservation.html", {"reservation": reservation})

    else:
        form = Reservation()
        messages.add_message(request, messages.INFO, "Ingrese los datos para realizar la Reserva")
        return render(request, "reservation/create_reservation.html", {"form": form})


# Client cancel reservation in the Room
@login_required
def cancel_reservation(request, id):
    if request.method == "POST":

        room = Room()

        reservation = Reservation.objects.get(pk=id)
        reservation.delete()

        messages.add_message(request, messages.SUCCESS, f"La reserva en la Habitacion {room.number} se ha Cancelado")
        return render(request, "reservation/cancel_reservation.html")