# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 19:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('pais', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateField(default=datetime.date.today, null=True)),
            ],
            options={
                'verbose_name_plural': 'Autores',
                'verbose_name': 'Autor',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('autor', models.CharField(blank=True, max_length=50, null=True)),
                ('unidad', models.IntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('estado', models.CharField(help_text='Ingresa el estado del libro: "R = renta, V = venta"', max_length=2)),
                ('fecha', models.DateField(default=datetime.date.today, null=True)),
            ],
            options={
                'verbose_name_plural': 'Libros',
                'verbose_name': 'Libro',
            },
        ),
    ]
