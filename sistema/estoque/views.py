from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Produto
# Create your views here.

def index(request):
    return render(request, "estoque/index.html",{})

def hora(request):
    context = {"hora":datetime.now()}
    return render(request, "estoque/hora.html", context)


def listagem(request):
    produtos = Produto.objects.all() 
    return render(request,'estoque/estoque.html',{'produtos':produtos})
