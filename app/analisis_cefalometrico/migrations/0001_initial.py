# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-23 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='analisis_cefalometrico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sna', models.FloatField(blank=True, null=True)),
                ('snb', models.FloatField(blank=True, null=True)),
                ('anb', models.FloatField(blank=True, null=True)),
                ('convexidad', models.FloatField(blank=True, null=True)),
                ('wits', models.FloatField(blank=True, null=True)),
                ('long_cuerpo_mandibular', models.FloatField(blank=True, null=True)),
                ('profundidad_maxilar', models.FloatField(blank=True, null=True)),
                ('profundidad_facial', models.FloatField(blank=True, null=True)),
                ('plano_mandibular', models.FloatField(blank=True, null=True)),
                ('eje_y_fh', models.FloatField(blank=True, null=True)),
                ('cono_facial', models.FloatField(blank=True, null=True)),
                ('eje_facial', models.FloatField(blank=True, null=True)),
                ('angulo_goniaco_superior', models.FloatField(blank=True, null=True)),
                ('angulo_goniaco_inferior', models.FloatField(blank=True, null=True)),
                ('angulo_goniaco_total', models.FloatField(blank=True, null=True)),
                ('is_na', models.FloatField(blank=True, null=True)),
                ('is_sn', models.FloatField(blank=True, null=True)),
                ('isfh', models.FloatField(blank=True, null=True)),
                ('impa', models.FloatField(blank=True, null=True)),
                ('protusion_de_incisivo_max', models.FloatField(blank=True, null=True)),
                ('protusion_de_incisivo_md', models.FloatField(blank=True, null=True)),
                ('protusion_labial', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
