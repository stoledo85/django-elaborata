from django.contrib import admin

from .models import Cidade, Cliente, Endereco

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Cliente)
