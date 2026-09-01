from django.contrib import admin
from django.urls import path
from .views import ListMenuItem, DetailMenuItem, CreateMenuItem, ModifyMenuItem, DeleteMenuItem


app_name = "menu_item"

urlpatterns = [
    path('list/', ListMenuItem.as_view(), name="list_item"),
    path('detail/<int:pk>/', DetailMenuItem.as_view(), name="detail_item"),
    path('create/', CreateMenuItem.as_view(), name="create_item"),
    path('modify/<int:pk>/', ModifyMenuItem.as_view(), name="modify_item"),
    path('delete/<int:pk>/', DeleteMenuItem.as_view(), name="delete_item"),
    path('admin/', admin.site.url)
]