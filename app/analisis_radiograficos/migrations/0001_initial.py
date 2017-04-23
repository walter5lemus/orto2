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
            name='aspectos_articulares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condilo_mand_izq_alto', models.FloatField()),
                ('condilo_mand_izq_ancho', models.FloatField()),
                ('condilo_mand_der_alto', models.FloatField()),
                ('condilo_mand_der_ancho', models.FloatField()),
                ('condilo_mand_simetrico', models.IntegerField(choices=[(1, b'Sim\xc3\xa9trico'), (2, b'Asim\xc3\xa9trico')], default=1)),
                ('condilo_mand_aspectos_observados', models.CharField(max_length=50)),
                ('eminencia_izq', models.FloatField()),
                ('eminencia_der', models.FloatField()),
                ('eminencia_simetrico', models.IntegerField(choices=[(1, b'Sim\xc3\xa9trico'), (2, b'Asim\xc3\xa9trico')], default=1)),
                ('eminencia_aspectos_observados', models.CharField(max_length=50)),
                ('espacio_articular_simetrico', models.IntegerField(choices=[(1, b'Sim\xc3\xa9trico'), (2, b'Asim\xc3\xa9trico')], default=1)),
                ('espacio_articular_aspectos_observados', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='aspectos_mandibulares2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aspectos_sinusales_simetrico', models.BooleanField(choices=[(True, 'Simetria'), (False, 'Asimetria')], default=True)),
                ('aspectos_sinusales_izq_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('aspectos_sinusales_der_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('ord_ori_simetrico', models.BooleanField(choices=[(True, 'Simetria'), (False, 'Asimetria')], default=True)),
                ('ord_ori_izq_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('ord_ori_der_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('fpgd_fpgi_simetrico', models.BooleanField(choices=[(True, 'Simetria'), (False, 'Asimetria')], default=True)),
                ('fpgd_fpgi_izq_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('fpgd_fpgi_der_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('veloc_erup_simetrico', models.BooleanField(choices=[(True, 'Simetria'), (False, 'Asimetria')], default=True)),
                ('veloc_erup_izq_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('veloc_erup_der_aspect_observ', models.CharField(blank=True, max_length=20, null=True)),
                ('diagnostico', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='estadios_de_nolla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_1_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_1_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_2_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_3_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('e_4_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('otros_hallazgos', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='secuencia_y_cronologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_1_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_1_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_2_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_3_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('o_4_8', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
