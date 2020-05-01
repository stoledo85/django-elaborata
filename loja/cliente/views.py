from django.shortcuts import render
from django.http import HttpResponse
from .forms import CidadeForm
from .forms import EnderecoForm
from .forms import ClienteForm
# Create your views here.
from datetime import datetime
from .models import Cliente


def index(request):
    return render(request, "cliente/index.html", {})


def hora(request):
    context = {"hora": datetime.now()}

    return render(request, "cliente/hora.html", context)


def listagem(request):
    clientes = Cliente.objects.all()
    return render(request, "cliente/listagem.html", {'clientes': clientes})


def cidadeView(request):
    context = {}
    form = CidadeForm()
    context['form'] = form
    if request.method == "POST":
        resultado = CidadeForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Salvo com Sucesso!"
            context['sucesso'] = sucesso
        else:
            erro = "Erro! Cadastro não salvo."
            context['erro'] = erro
    return render(request, "cliente/cidade.html", context)


def enderecoView(request):
    context = {}
    form = EnderecoForm()
    context['form'] = form
    if request.method == "POST":
            resultado = EnderecoForm(request.POST)
            if resultado.is_valid():
                resultado.save()
                sucesso = "Endereço Salvo com Sucesso"
                context["sucesso"] = sucesso
            else:
                erro = "Endereço não foi salvo"
                context["erro"] = erro
    return render(request, "cliente/endereco.html", context)

# Cadastro de Clientes


def clienteView(request):
    context = {}
    form = ClienteForm()
    context['form'] = form
    if request.method == "POST":
        resultado = ClienteForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Cliente Salvo com Sucesso"
            context["sucesso"] = sucesso
        else:
            erro = "Cliente nao foi salvo"
            context["erro"] = erro
    return render(request, "cliente/cliente.html", context)


def clienteBuscaView(request):
    pass
