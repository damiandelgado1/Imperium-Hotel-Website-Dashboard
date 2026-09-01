from django.db import models


# Information of the Food and Menu Item in the Restaurant
class Menu_Item(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre de la Comida")
    stock = models.IntegerField(verbose_name="Stock de la Comida")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio de la Comida")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "menu_items"
        verbose_name_plural = "menu_item"