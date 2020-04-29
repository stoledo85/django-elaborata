from django.db import models

"""Subclasse de Endereço"""


class Cidade(models.Model):
    nomeCidade = models.CharField(verbose_name="Cidade", max_length=15)
    nomeUF = models.CharField(verbose_name="Estado", max_length=2)

    def __str__(self):
        return self.nomeCidade+" - " + self.nomeUF


"""Modelo de Entedeço"""


class Endereco(models.Model):
    logradouroEndereco = models.CharField(
        verbose_name="Endereço do Cliente", max_length=40)
    nroEndereco = models.IntegerField(verbose_name="Número do Cliente")
    nomeBairro = models.CharField(verbose_name="Bairro", max_length=45)
    # TODO Transformar essa relação many to many.
    cidadeEndereco = models.ForeignKey(
        Cidade, verbose_name="Cidade", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.logradouroEndereco



"""Construção do Modelo do Cliente."""

class Cliente(models.Model):
    nomeCliente = models.CharField(
        verbose_name="Nome do Cliente", max_length=45)
    numeroCpf = models.CharField(verbose_name="Número do CPF", max_length=14)
    dataNascimento = models.DateField(verbose_name="Data de Nascimento")
    idade = models.IntegerField(verbose_name="Idade")
    # TODO Transformar essa relação many to many.
    codigoEndereco = models.ForeignKey(
        Endereco, verbose_name=("Endereço"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeCliente
    