# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
        ('gestorImg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='img_radiograficas',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='img_paciente2',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='img_paciente',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
    ]
