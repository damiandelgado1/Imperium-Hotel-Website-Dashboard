from django import forms


# Contact Client to Hotel
class Contact(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()


# Register Client in the Hotel
class Register(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    is_properly = forms.BooleanField(required=False, label="¿Es Propietario?")
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


# Login Client in the Hotel
class Login(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")