from django.db import models
from menu_item.models import Menu_Item


# Information of the Order made of the Client
class Order(models.Model):
    name = models.ForeignKey(Menu_Item, on_delete=models.CASCADE, verbose_name="Orden del Cliente")
    amount = models.IntegerField(verbose_name="Cantidad de la Orden del Cliente")
    payment = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Pago de la Orden")

    def __str__(self):
        return f"{self.name} {self.client} {self.amount}"

    class Meta:
        verbose_name = "orders"
        verbose_name_plural = "order"