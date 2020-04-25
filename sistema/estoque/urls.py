from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    path("", views.index, name="index"),
    path('hora/', views.hora, name="hora"),
    path('listagem/', views.listagem, name='listagem')
]
