# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cita', models.IntegerField()),
                ('fecha_cita', models.DateField()),
                ('observaciones', models.CharField(max_length=250)),
                ('proxima_cita', models.DateField()),
                ('resultados', models.CharField(max_length=250)),
                ('autorizacion', models.BooleanField()),
                ('tutor', models.CharField(blank=True, max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='citas_general',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aparato', models.IntegerField(choices=[(1, b'Ortodoncia Fija'), (2, b'Boton de Nance'), (3, b'Boton de Nance'), (4, b'Arco Lingua'), (5, b'Tornillo Hirax'), (6, b'Barra Transpalatina'), (7, b'Botones'), (8, b'SN1'), (9, b'SN2'), (10, b'SN3'), (11, b'SN4'), (12, b'SN5'), (13, b'SN6'), (14, b'SN7'), (15, b'SN8'), (16, b'SN9'), (17, b'SN10'), (18, b'Pistas Planas Directas'), (19, b'Pistas Planas Indirectas'), (20, b'Aparato Bimler'), (21, b'Bionator'), (22, b'Otros')])),
                ('mx', models.BooleanField()),
                ('md', models.BooleanField()),
            ],
        ),
    ]
