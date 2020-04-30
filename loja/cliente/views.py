from django.shortcuts import render
from django.http import HttpResponse
from .forms import CidadeForm
from .forms import EnderecoForm
from .forms import ClienteForm
# Create your views here.
from datetime import datetime

def index(request):
    return render(request, "cliente/index.html",{})


def hora(request):
    context = {"hora":datetime.now()}
    
    return render(request, "cliente/hora.html", context)

def pessoa(request):
    pessoa = {"nome": 'Sander', "nascimento":'10/06/1985', "email":'sander@algumacoisa.com.br',"telefone":'123456789'}
    
    return render(request, "cliente/pessoa.html", pessoa)

def cidadeView(request):
    
    if request.method == "GET":
        form = CidadeForm()
        context = {"form":form}
        return render(request, "cliente/cidade.html", context)
    elif request.method == "POST":
        pass


    
def enderecoView(request):
    form = EnderecoForm()
    context = {"form":form}
    return render(request, "cliente/endereco.html", context)

def clienteView(request):
    form = ClienteForm()
    context = {"form":form}
    return render(request, "cliente/cliente.html", context)