from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["client", "room", "people", "enter", "exit"]
    list_filter = ["client", "room", "enter", "exit"]
    search_fields = ["client", "room"]