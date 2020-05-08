# Generated by Django 3.0.5 on 2020-04-19 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCategoria', models.CharField(max_length=15, verbose_name='Nome da Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeMarca', models.CharField(max_length=15, verbose_name='Nome da Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(max_length=20, verbose_name='Nome do Produto')),
                ('descProduto', models.TextField(verbose_name='Descrição do Produto')),
                ('precoProduto', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Preço Unitario')),
                ('categoriaProduto', models.ManyToManyField(to='estoque.Categoria', verbose_name='Categoria')),
                ('marcaProduto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estoque.Marca', verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codProduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto', verbose_name='Codigo Produto')),
            ],
        ),
    ]