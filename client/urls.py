from django.contrib import admin
from django.urls import path
from .views import contact, register, login, logout


app_name = "client"

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('admin/', admin.site.urls),
]