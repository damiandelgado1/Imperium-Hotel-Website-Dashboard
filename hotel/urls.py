from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('client/', include("client.urls", namespace="client")),
    path('room/', include("room.urls", namespace="room")),
    path('reservation/', include("reservation.urls", namespace="reservation")),
    path('order/', include("order.urls", namespace="order")),
    path('menu_item/', include("menu_item.urls", namespace="menu_item")),
    path('admin/', admin.site.urls),
]