from django.forms import forms

# Contact Client to Hotel
class Contact(forms.Form):
    first_name = forms.CharField(max_length=20, verbose_name="Nombre del Cliente")
    last_name = forms.CharField(max_length=20, verbose_name="Apellido del Cliente")
    email = forms.EmailField(verbose_name="Email del Cliente")


# Register Client in the Hotel
class Register(forms.Form):
    first_name = forms.CharField(max_length=20, verbose_name="Nombre del Cliente")
    last_name = forms.CharField(max_length=20, verbose_name="Apellido del Cliente")
    username = forms.CharField(max_length=20, verbose_name="Nombre de Usuario del Cliente")
    email = forms.EmailField(verbose_name="Email del Cliente")
    password1 = forms.CharField(widget=forms.PasswordInput, verbose_name="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, verbose_name="Confirmacion de Contraseña")
    is_properly = forms.BooleanField(verbose_name="¿Es propietario?")


# Login Client in the Hotel
class Login(forms.Form):
    username = forms.CharField(max_length=20, verbose_name="Nombre de Usuario del Cliente")
    password2 = forms.CharField(widget=forms.PasswordInput, verbose_name="Contraseña de Inicio del Cliente")