from django.forms import ModelForm
from .models import Cidade
from .models import Endereco
from .models import Cliente

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
        fields = ['nomeCliente', 'numeroCpf', 'dataNascimento', 'idade', 'codigoEndereco']
        