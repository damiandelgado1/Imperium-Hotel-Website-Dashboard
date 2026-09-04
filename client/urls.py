from django.contrib import admin
from django.urls import path
from .views import contact, register_client, login_client, logout_client


app_name = "client"

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('register/', register_client, name="register_client"),
    path('login/', login_client, name="login_client"),
    path('logout/', logout_client, name="logout_client"),
    path('admin/', admin.site.urls),
]