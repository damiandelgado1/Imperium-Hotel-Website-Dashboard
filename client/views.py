from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
                messages.add(request, messages.INFO, 'Falta un @ en el Email')
                return render(request, "")

            else:
                context = {
                    "Nombre": first_name,
                    "Apellido": last_name,
                    "Email": email
                }

                messages.add(request, messages.SUCCESS, 'Gracias por Contactar al Hotel, su respuesta llegara pronto')
                return render(request, "", context)

        else:
            form = Register()
            messages.add(request, messages.INFO, 'Indique sus datos de contacto para contactar al Hotel')


# Client register in the Hotel to create Account
def register(request):
    if request.method == "POST":

        form = Register(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            is_properly = form.cleaned_data["is_properly"]

            if "@" not in email:
                messages.add(request, messages.INFO, 'Falta el "@" en el Email')
                return render(request, "")

            elif password2 != password1:
                messages.add(request, messages.INFO, 'La contraseña debe ser la misma')
                return render(request, "")

            elif password2 == "":
                messages.add(request, messages.INFO, 'Debe ingresar la contraseña de confirmacion')
                return render(request, "")

            else:
                client = User.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password1 = password1,
                    password2 = password2,
                    is_properly = is_properly
                )

                messages.add(request, messages.INFO, 'Registro completado')
                return render(request, "", client)

        else:
            form = Register()
            messages.add(request, messages.INFO, 'Indique sus datos para Registrarse')
            return render(request, "")


# Client login in the Account
def login(request):
    if request.method == "POST":

        form = Login(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password2 = form.cleaned_data["password2"]

            user = authenticate(user, username=username, password2=password2)

            if user is not None:
                login(user, request)
                messages.add(request, messages.SUCCESS, 'Inicio de Sesion realizado')
                return render(request, "")

            else:
                messages.add(request, messages.INFO, 'El cliente que intenta Iniciar Sesion no existe')
                return render(request, "")

        else:
            form = Login()
            messages.add(request, messages.INFO, 'Indique su informacion para Iniciar Sesion')
            return render(request, "")


# Client logout of the Account in the Hotel
def logout(request):
    logout(reverse_lazy(request))
    return redirect("home")