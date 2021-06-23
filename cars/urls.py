from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing, name="landing"),
    path('add_car/', views.add_car, name="add_car"),
    path('delete_car/<str:pk>', views.delete_car, name="delete_car"),
    path('update_car/<str:pk>', views.update_car, name="update_car"),
]