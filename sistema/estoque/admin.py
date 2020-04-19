from django.contrib import admin
from .models import Categoria
from .models import Estoque
from .models import Marca
from .models import Produto
# Register your models here.


admin.site.register(Categoria)
admin.site.register(Estoque)
admin.site.register(Marca)
admin.site.register(Produto)
