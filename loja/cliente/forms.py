from django import forms
from django.forms import ModelForm

from .models import Cidade, Cliente, Endereco


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ['nomeCidade', 'nomeUF']
        help_texts = {
            "nomeCidade":"Nome de Cidade",
            "nomeUF":"Unidade Federativa ou Estado"
        }
        labels = {
            "nomeCidade":"Cidade",
            "nomeUF":"UF"
        }
        error_messages={
        "nomeCidade":{"max_length" : "nao pode ser superior a 15 caracteres,"}
        }

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouroEndereco','nroEndereco', 'nomeBairro', 'cidadeEndereco' ]
        help_texts={
            'logradouroEndereco':'Favor informar o nome da Rua.',
            'nroEndereco':'Digitar o numero da casa ou apartamento.',
            'nomeBairro':'Informar o bairro.'
        }
        labels = {
            'logradouroEndereco':'Logradouro', 
            'nroEndereco':'Número',
            'nomeBairro':'Bairro',
            'cidadeEndereco':'Cidade',
        }
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nomeCliente':'Nome', 'numeroCpf':'CPF', 'dataNascimento':'Data de Nascimento', 'codigoEndereco':"Endereço"]
        
class BuscaClienteForm(forms.Form):
    nomeCliente = forms.CharField( max_length=45)
    dataNascimento = forms.CharField(max_length=10)
