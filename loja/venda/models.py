from django.db import models

from cliente.models import Cliente
from estoque.models import Produto
# Create your models here.


class Venda(models.Model):

    codigoVenda = models.AutoField(verbose_name="Código do Cliente", primary_key=True, serialize=True)
    codigoCliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT)
    codigoProduto = models.ForeignKey(Produto, verbose_name=("Produto"), on_delete=models.PROTECT)
    vendaQntde = models.IntegerField(verbose_name='Quantidade')
    vendaSub = models.DecimalField(verbose_name='Subtotal', max_digits=5, decimal_places=2)
    