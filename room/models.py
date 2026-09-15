from django.db import models


# Data and Specification a Room in the Hotel
class Room(models.Model):
    number = models.IntegerField(verbose_name="Nro. de la Habitacion")
    preview = models.TextField(verbose_name="Descripcion de Previsualizacion")
    description = models.TextField(verbose_name="Descripcion de la Habitacion")
    bedroom = models.IntegerField(verbose_name="Nro. de Dormitorios")
    bathroom = models.IntegerField(verbose_name="Nro. de Baños")
    availability = models.CharField(max_length=20, verbose_name="Disponibilidad de la Habitacion")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio de la Habitacion")

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "rooms"
        verbose_name_plural = "room"