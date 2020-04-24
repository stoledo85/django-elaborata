from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.index, name="index"),
    path('hora/', views.hora, name="hora"),
    path('pessoa/', views.pessoa, name="pessoa")
]
