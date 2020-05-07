from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .forms import CategoriaForm, MarcaForm, ProdutoForm
from .models import Produto

# Create your views here.

def index(request):
    return render(request, "estoque/index.html",{})

def hora(request):
    context = {"hora":datetime.now()}
    return render(request, "estoque/hora.html", context)

"""
    Gerar Uma Lista de Todos os produtos disponiveis em cadastro
"""
def listagem(request):
    produtos = Produto.objects.all() 
    return render(request,'estoque/estoque.html',{'produtos':produtos})


def produtoView(request):
    context = {}
    form = ProdutoForm()
    context['form'] = form
    if request.method == "POST":
        resultado = procutoForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Salvo com Sucesso!"
            context['sucesso'] = sucesso
        else:
            erro = "Erro! Cadastro não salvo."
            context['erro'] = erro
    return render(request, "estoque/produto.html", context)

def marcaView(request):
    context = {}
    form = MarcaForm()
    context['form'] = form
    if request.method == "POST":
        resultado = MarcaForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Salvo com Sucesso!"
            context['sucesso'] = sucesso
        else:
            erro = "Erro! Cadastro não salvo."
            context['erro'] = erro

    return render(request, "estoque/marca.html", context)

def categoriaView(request):
    context = {}
    form = CategoriaForm()
    context['form'] = form
    if request.method == "POST":
        resultado = CategoriaForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Salvo com Sucesso!"
            context['sucesso'] = sucesso
        else:
            erro = "Erro! Cadastro não salvo."
            context['erro'] = erro
    return render(request, "estoque/categoria.html", context)
