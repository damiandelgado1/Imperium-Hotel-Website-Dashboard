from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Client
from .forms import Contact, Register, Login


# Client contact Hotel Website to obtain more Information
def contact(request):
    if request.method == "POST":

        form = Contact(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            if "@" not in email:
                messages.add_message(request, messages.INFO, 'Falta un @ en el Email')
                return render(request, "home/base.html")

            else:
                context = {
                    "Nombre": first_name,
                    "Apellido": last_name,
                    "Email": email
                }

                messages.add_message(request, messages.SUCCESS, 'Gracias por Contactar al Hotel, su respuesta llegara pronto')
                return render(request, "home/base.html", context)

        else:
            messages.add_message(request, messages.INFO, 'Revisa los datos ingresados')
            return render(request, "home/register.html", {"form": form})

    else:
        form = Contact()
        messages.add_message(request, messages.INFO, 'Indique sus datos de contacto para contactar al Hotel')
        return render(request, "home/base.html", {"form": form})


# Client register in the Hotel to create Account
def register_client(request):
    if request.method == "POST":

        form = Register(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            is_properly = form.cleaned_data["is_properly"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if "@" not in email:
                messages.add_message(request, messages.INFO, 'Falta el "@" en el Email')
                return render(request, "home/register.html")

            elif password2 != password1:
                messages.add_message(request, messages.INFO, 'La contraseña debe ser la misma')
                return render(request, "home/register.html")

            elif password2 == "":
                messages.add_message(request, messages.INFO, 'Debe ingresar la contraseña de confirmacion')
                return render(request, "home/register.html")

            else:
                client = Client.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password1 = password1,
                    password2 = password2,
                    is_properly = is_properly
                )

                messages.add_message(request, messages.INFO, 'Registro completado')
                return render(request, "home/base.html", {"client": client})

        else:
            messages.add_message(request, messages.INFO, 'Revisa los datos ingresados')
            return render(request, "home/register.html", {"form": form})

    else:
        form = Register()
        messages.add_message(request, messages.INFO, 'Indique sus datos para Registrarse')
        return render(request, "home/register.html", {"form": form})


# Client login in the Account
def login_client(request):
    if request.method == "POST":

        form = Login(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password2 = form.cleaned_data["password2"]

            user = authenticate(request, username=username, password=password2)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Inicio de Sesion realizado')
                return render(request, "home/login.html")

            else:
                messages.add_message(request, messages.INFO, 'El cliente que intenta Iniciar Sesion no existe')
                return render(request, "home/base.html", {"form": form})

        else:
            messages.add_message(request, messages.INFO, 'Revisa los datos ingresados')
            return render(request, "home/login.html", {"form": form})

    else:
        form = Login()
        messages.add_message(request, messages.INFO, 'Indique su informacion para Iniciar Sesion')
        return render(request, "home/login.html", {"form": form})


# Client logout of the Account in the Hotel
def logout_client(request):
    logout(request)
    return redirect("home")