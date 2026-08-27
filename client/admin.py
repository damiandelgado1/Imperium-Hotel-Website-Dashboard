from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "username", "email", "is_properly"]
    list_filter = ["first_name", "last_name", "username", "email"]
    search_fields = ["first_name", "last_name", "email"]