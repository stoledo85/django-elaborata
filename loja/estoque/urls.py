from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    path("", views.index, name="index"),
    path('hora/', views.hora, name="hora"),
    path('listagem/', views.listagem, name='listagem'),
    path("produto/", views.produtoView, name='produto'),
    path("marca/", views.marcaView, name="marca"),
    path("categoria/", views.categoriaView, name="categoria"),
]
