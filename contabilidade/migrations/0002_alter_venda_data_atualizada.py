# Generated by Django 5.2 on 2025-05-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_atualizada',
            field=models.DateField(auto_now_add=True, verbose_name='Atualizacao'),
        ),
    ]
