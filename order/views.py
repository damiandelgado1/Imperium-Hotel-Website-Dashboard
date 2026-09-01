from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Order


# Display all Order create by the Client in the Hotel
class ListOrder(ListView):
    model = Order
    template_name = ""
    context_object_name = "orders"


# Show specification a Order created by the Client
class DetailOrder(DetailView):
    model = Order
    template_name = ""
    context_object_name = "order"


# Create a Order in the Hotel Restaurant
@login_required
def create_order(request):
    if request.method == "POST":

        form = Order(request.POST)

        if form.is_valid():
            order = form.cleaned_data["order"]
            amount = form.cleaned_data["amount"]
            state = form.cleaned_data["state"]
            payment = form.cleaned_data["payment"]

            if payment < product.price:
                messages.add(request, messages.INFO, "El pago por la Orden es bajo")
                return render(request, "")

            else:
                order = Order.objects.create(
                    order = order,
                    amount = amount,
                    state = state,
                    payment = payment
                )
                messages.add(request, messages.SUCCESS, "La orden se ha creado correctamente")
                return render(request, "", order)

        else:
            form = Order()
            messages.add(request, messages.INFO, "Indique la Orden que va a pedir")
            return render(request, "")


# Cancel a Order in the Hotel Restaurant
@login_required
def cancel_order(request, id):
    if request.method == "POST":

        order = Order.objects.get(pk=id)
        order.delete()

        messages.add(request, messages.SUCCESS, "La orden fue cancelada")
        return render(request, "")