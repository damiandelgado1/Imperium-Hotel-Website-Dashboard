from django.contrib import admin
from django.urls import path
from .views import ListOrder, DetailOrder, create_order, cancel_order


app_name = "order"

urlpatterns = [
    path('list/', ListOrder.as_view(), name="list_order"),
    path('detail/<int:pk>/', DetailOrder.as_view(), name="detail_order"),
    path('create/', create_order, name="create_order"),
    path('delete/<int:pk>/', cancel_order, name="delete_order"),
    path('admin/', admin.site.urls)
]