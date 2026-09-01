from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order", "amount", "state", "price"]
    list_filter = ["order", "state", "price"]
    search_fields = ["order"]