from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from .models import Produto

from .forms import ProdutoForm
from .forms import MarcaForm
from .forms import CategoriaForm
# Create your views here.

def index(request):
    return render(request, "estoque/index.html",{})

def hora(request):
    context = {"hora":datetime.now()}
    return render(request, "estoque/hora.html", context)


def listagem(request):
    produtos = Produto.objects.all() 
    return render(request,'estoque/estoque.html',{'produtos':produtos})


def produtoView(request):
    form = ProdutoForm()
    context = {"form":form}
    return render(request, "estoque/produto.html", context)

def marcaView(request):
    form = MarcaForm()
    context = {"form":form}
    return render(request, "estoque/marca.html", context)

def categoriaView(request):
    form = CategoriaForm()
    context = {"form":form}
    return render(request, "estoque/categoria.html", context)