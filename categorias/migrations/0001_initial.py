# Generated by Django 2.0.4 on 2018-04-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisao', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('MASC', 'Masculino'), ('FEM', 'Feminino')], max_length=10)),
                ('tipo', models.CharField(choices=[('RAT', 'Rating'), ('RANK', 'Ranking')], max_length=10)),
                ('modalidade', models.CharField(choices=[('OLIM', 'Olimpico'), ('PARAOLIM', 'Paraolimpico')], max_length=12)),
            ],
        ),
    ]
