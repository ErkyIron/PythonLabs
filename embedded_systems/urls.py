from django.urls import path
from . import views

urlpatterns = [
    path("", views.embedded_systems_index, name="embedded_systems_index"),
    path('clear/', views.clear_commands, name='clear_commands'),
]