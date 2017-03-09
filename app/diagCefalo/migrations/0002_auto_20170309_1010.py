# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-09 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
        ('diagCefalo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico_cefalometrico',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='diagnostico_cefalometrico',
            name='medidas_dentales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diagCefalo.MDentales'),
        ),
        migrations.AddField(
            model_name='diagnostico_cefalometrico',
            name='patron_esqueletal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diagCefalo.Patron'),
        ),
        migrations.AddField(
            model_name='diagnostico_cefalometrico',
            name='tipo_de_crecimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diagCefalo.Crecimiento'),
        ),
    ]
