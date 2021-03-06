# Generated by Django 2.0.4 on 2018-04-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='modalidade',
            field=models.CharField(choices=[('OLIM', 'Olimpico'), ('PARAOLIM', 'Paraolimpico')], default='OLIM', max_length=12),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='sexo',
            field=models.CharField(choices=[('MASC', 'Masculino'), ('FEM', 'Feminino')], default='MASC', max_length=10),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(choices=[('RAT', 'Rating'), ('RANK', 'Ranking')], default='RAT', max_length=10),
        ),
    ]
