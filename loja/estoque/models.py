from django.db import models

# Create your models here.

# TODO Implementar o modelo de estoque.


class Marca(models.Model):

    nomeMarca = models.CharField(verbose_name="Nome da Marca", max_length=15)

    def __str__(self):
        return self.nomeMarca


class Categoria(models.Model):

    nomeCategoria = models.CharField(
        verbose_name="Nome da Categoria", max_length=15)
    # TODO Implementar a lista de produtos relacionada a esta marca.
    produtoCategoria = None

    def __str__(self):
        return self.nomeCategoria


class Produto(models.Model):

    nomeProduto = models.CharField(verbose_name="Nome do Produto", max_length=20)
    descProduto = models.TextField(verbose_name="Descrição do Produto")
    # Existe uma função do python que retorna o valor local. Locate.
    precoProduto = models.DecimalField(verbose_name="Preço Unitario", max_digits=8, decimal_places=2)
    categoriaProduto = models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.CASCADE)
    marcaProduto = models.ForeignKey(Marca, verbose_name="Marca", on_delete=models.PROTECT)

    def __str__(self):
        return self.nomeProduto 
    

""" class Estoque(models.Model):
    codProduto = models.ForeignKey(Produto, verbose_name="Codigo Produto", on_delete=models.CASCADE)
    dataMovimentacao = models.DateTime(verbose_name="Data da Movimentação")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    tipo """