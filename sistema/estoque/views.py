from django.shortcuts import render
from django.http import HttpResponse

from .models import Produto
# Create your views here.

def index(request):
    return render(request, "estoque/index.html",{})



def listagem(request):
    produto = Produto.objects.all()
    
    return render(request,'produto.html',{'produtos':produto})
