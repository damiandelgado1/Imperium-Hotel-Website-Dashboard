from django.db import models
from django.contrib.auth.models import User
from room.models import Room


# Information of Reservation the a Client
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Habitacion reservada por el Cliente")
    people = models.IntegerField(verbose_name="Nro. de Personas que entran en la Habitacion")
    enter = models.DateField(verbose_name="Fecha de Entrada")
    exit = models.DateField(verbose_name="Fecha de Salida")
    payment = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Pago del Cliente por la Habitacion")

    def __str__(self):
        return f"Habitacion {self.room} reservada"

    class Meta:
        verbose_name = "reservations"
        verbose_name_plural = "reservation"