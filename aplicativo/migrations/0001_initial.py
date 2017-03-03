# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('cnes', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('home', models.CharField(max_length=60)),
                ('razaoSocial', models.CharField(max_length=100)),
                ('atendeSus', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TipoGestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('sigla', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicativo.Uf'),
        ),
        migrations.AddField(
            model_name='estabelecimento',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicativo.Municipio'),
        ),
        migrations.AddField(
            model_name='estabelecimento',
            name='tipoGestao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicativo.TipoGestao'),
        ),
    ]
