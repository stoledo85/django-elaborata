from django.forms import ModelForm
from .models import Cidade
from .models import Endereco
from .models import Cliente

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = "__all__"

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"