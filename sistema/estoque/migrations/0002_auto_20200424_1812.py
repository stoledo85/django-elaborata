# Generated by Django 3.0.5 on 2020-04-24 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoriaProduto',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoriaProduto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estoque.Categoria', verbose_name='Categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='precoProduto',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço Unitario'),
        ),
    ]
