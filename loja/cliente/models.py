from django.db import models

#Subclasse de Endereço
class Cidade(models.Model):
    nomeCidade = models.CharField(verbose_name="Cidade",max_length=15)
    nomeUF = models.CharField(verbose_name="Estado", max_length=2)

#Modelo de Entedeço
class Endereco(models.Model):
    ruaEndereco  = models.CharField( verbose_name="Endereço do Cliente",max_length=80)
    nroEndereco = models.IntegerField( verbose_name="Numero do Cliente")
    nomeBairro = models.CharField( verbose_name="Nome do Cliente",max_length=45)
    cidadeEndereco = models.ForeignKey(Cidade,verbose_name="Cidade", on_delete=models.PROTECT)#TODO Transformar essa relação many to many.

#Construção do Modelo do Cliente.
class Cliente(models.Model):
    nomeCliente = models.CharField( verbose_name="Nome do Cliente",max_length=45)
    numeroCpf = models.CharField(verbose_name="Número do CPF" ,max_length=14)
    dataNascimento = models.DateField(verbose_name="Data de Nascimento")
    idade = models.IntegerField(verbose_name="Idade")
    codigoEndereco = models.ForeignKey(Endereco, verbose_name=("Endereço"), on_delete=models.CASCADE)#TODO Transformar essa relação many to many.


