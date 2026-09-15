from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["room", "people", "enter", "exit"]
    list_filter = ["room", "enter", "exit"]
    search_fields = ["room"]