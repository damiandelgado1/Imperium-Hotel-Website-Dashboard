from django.db import models

# Information of the Order made of the Client
class Order(models.Model):
    order = models.ForeignKey(, on_delete=models.CASCADE, verbose_name="Orden del Cliente")
    amount = models.IntegerField(verbose_name="Cantidad de la Orden del Cliente")
    state = models.CharField(max_length=20, verbose_name="Estado de la Orden")
    payment = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Pago de la Orden")

    def __str__(self):
        return f"{self.order} {self.state} {self.price}"

    class Meta:
        verbose_name = "orders"
        verbose_name_plural = "order"