from django.contrib import admin
from django.urls import path
from .views import ListRoom, DetailRoom, ManageRoom, EditRoom, CreateRoom, ModifyRoom, DeleteRoom


app_name = "client"

urlpatterns = [
    path('list/', ListRoom.as_view(), name="list_room"),
    path('detail/<int:pk>/', DetailRoom.as_view(), name="detail_room"),
    path('manage/', ManageRoom.as_view(), name="manage_room"),
    path('edit/<int:pk>/', EditRoom.as_view(), name="edit_room"),
    path('create/', CreateRoom.as_view(), name="create_room"),
    path('modify/<int:pk>/', ModifyRoom.as_view(), name="modify_room"),
    path('delete/<int:pk>/', DeleteRoom.as_view(), name="delete_room"),
    path('admin/', admin.site.urls),
]