# Generated by Django 5.2 on 2025-04-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedoras', '0005_representantes_bairro_representantes_cep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representantes',
            name='bairro',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='representantes',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='representantes',
            name='cidade',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='representantes',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='representantes',
            name='rua',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
