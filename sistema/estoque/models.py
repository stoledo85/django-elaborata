from django.db import models

# Create your models here.

# TODO Implementar o modelo de estoque.

class Marca(models.Model):

    nomeMarca = models.CharField(verbose_name="Nome da Marca", max_length=15)

class Categoria(models.Model):
    
    nomeCategoria = models.CharField(verbose_name="Nome da Categoria", max_length=15)
    produtoCategoria = None #TODO Implementar a lista de produtos relacionada a esta marca.

    
class Produto(models.Model):

    nomeProduto = models.CharField(verbose_name="Nome do Produto", max_length=20)
    descProduto = models.TextField(verbose_name="Descrição do Produto")
    precoProduto = models.DecimalField(verbose_name="Preço Unitario", max_digits=4, decimal_places=2)#Existe uma função do python que retorna o valor local. Locate.
    categoriaProduto = models.ManyToManyField(Categoria, verbose_name="Categoria")
    marcaProduto = models.ForeignKey(Marca, verbose_name="Marca", on_delete=models.PROTECT)