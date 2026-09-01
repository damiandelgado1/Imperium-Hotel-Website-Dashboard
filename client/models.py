from django.db import models

# Information of the Client
class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Nombre del Cliente")
    last_name = models.CharField(max_length=20, verbose_name="Apellido del Cliente")
    username = models.CharField(max_length=20, verbose_name="Nombre de Usuario")
    email = models.EmailField(verbose_name="Email del Cliente")
    is_properly = models.BooleanField()
    password1 = models.CharField(max_length=20, verbose_name="Contraseña del Cliente")
    password2 = models.CharField(max_length=20, verbose_name="Confirmacion de Contraseña")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"