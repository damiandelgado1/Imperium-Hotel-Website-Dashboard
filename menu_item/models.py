from django.db import models


# Information of the Food and Menu Item in the Restaurant
class Menu_Item(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre del Plato del Menu")
    description = models.TextField(verbose_name="Descripcion del Plato del Menu")
    availability = models.BooleanField(verbose_name="Disponibilidad del Plato del Menu")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio del Plato del Menu")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "items"
        verbose_name_plural = "item"