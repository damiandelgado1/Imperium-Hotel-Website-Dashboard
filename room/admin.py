from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["number", "preview", "description", "bedroom", "bathroom", "availability", "price"]
    list_filter = ["number", "availability", "price"]
    search_fields = ["number"]