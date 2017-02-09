# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moyers_inferior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ed_izquierdo', models.FloatField(blank=True, null=True)),
                ('ed_derecho', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='moyers_inferior_ancho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancho_mesiodistal', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='moyers_superior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ed_izquierdo', models.FloatField(blank=True, null=True)),
                ('ed_derecho', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='moyers_superior_ancho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancho_mesiodistal', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
