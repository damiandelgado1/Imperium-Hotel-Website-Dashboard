from django.contrib import admin
from django.urls import path, include
from .views import main_page, restaurant, about_us


urlpatterns = [
    path('', main_page, name="home"),
    path('restaurant/', restaurant, name="restaurant"),
    path('about_us/', about_us, name="about_us"),
    path('client/', include("client.urls", namespace="client")),
    path('room/', include("room.urls", namespace="room")),
    path('reservation/', include("reservation.urls", namespace="reservation")),
    path('order/', include("order.urls", namespace="order")),
    path('menu_item/', include("menu_item.urls", namespace="menu_item")),
    path('admin/', admin.site.urls),
]