from django.forms import ModelForm
from .models import Produto
from .models import Marca
from .models import Categoria

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"


