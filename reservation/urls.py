from django.contrib import admin
from django.urls import path
from .views import ListReservation, DetailReservation, create_reservation, cancel_reservation


app_name = "reservation"

urlpatterns = [
    path('list/', ListReservation.as_view(), name="list_reservation"),
    path('detail/<int:pk>/', DetailReservation.as_view(), name="detail_reservation"),
    path('create/', create_reservation, name="create_reservation"),
    path('delete/<int:pk>/', cancel_reservation, name="delete_reservation"),
    path('admin/', admin.site.urls),
]