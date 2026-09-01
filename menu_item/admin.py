from django.contrib import admin
from .models import Menu_Item


@admin.register(Menu_Item)
class Menu_ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "stock", "price"]
    list_filter = ["name", "stock"]
    search_fields = ["name"]