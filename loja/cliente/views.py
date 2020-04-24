from django.shortcuts import render
from django.http import HttpResponse
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