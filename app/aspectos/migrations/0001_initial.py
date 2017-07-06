# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='denticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal_posiciones', models.CharField(max_length=50)),
                ('tejido_intraorales', models.CharField(max_length=200)),
                ('encias', models.CharField(max_length=100)),
                ('frenillos', models.CharField(max_length=100)),
                ('lengua', models.CharField(max_length=100)),
                ('observaciones_generales', models.CharField(max_length=384)),
            ],
        ),
        migrations.CreateModel(
            name='diastemas_denticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuad_uno', models.IntegerField()),
                ('pieza_uno', models.IntegerField()),
                ('cuad_dos', models.IntegerField()),
                ('pieza_dos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='funcion_mandibular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apertura', models.IntegerField()),
                ('desv_afmp_derecho', models.IntegerField()),
                ('desv_afmp_izquierdo', models.IntegerField()),
                ('signos_sintomas_atm', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='imagenes_afmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreimagen', models.CharField(blank=True, default='Sin nombre', max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='afmp')),
            ],
        ),
        migrations.CreateModel(
            name='linea_media_facial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mx', models.IntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('mx_desviacion', models.IntegerField(choices=[(1, b'Derecha'), (2, b'Centrado'), (3, b'Izquierda')])),
                ('md', models.IntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('md_desviacion', models.IntegerField(choices=[(1, b'Derecha'), (2, b'Centrado'), (3, b'Izquierda')])),
            ],
        ),
        migrations.CreateModel(
            name='problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_problemas', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuadrante', models.IntegerField(blank=True, null=True)),
                ('pieza', models.IntegerField(blank=True, null=True)),
                ('detalle', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='registro_mordidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuad_superior', models.IntegerField()),
                ('pieza_superior', models.IntegerField()),
                ('cuad_inferior', models.IntegerField()),
                ('pieza_inferior', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='relaciones_sagitales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molar_derecha', models.IntegerField(blank=True, choices=[(1, b'Clase 1'), (2, b'Clase 2'), (3, b'Clase 3'), (4, b'CC'), (5, b'N.E.')], null=True)),
                ('molar_izquierda', models.IntegerField(blank=True, choices=[(1, b'Clase 1'), (2, b'Clase 2'), (3, b'Clase 3'), (4, b'CC'), (5, b'N.E.')], null=True)),
                ('canina_derecha', models.IntegerField(choices=[(1, b'Clase 1'), (2, b'Clase 2'), (3, b'Clase 3'), (4, b'CC'), (5, b'N.E.')])),
                ('canina_izquierda', models.IntegerField(choices=[(1, b'Clase 1'), (2, b'Clase 2'), (3, b'Clase 3'), (4, b'CC'), (5, b'N.E.')])),
                ('plano_termina_recto', models.IntegerField(blank=True, choices=[(1, b'Derecho'), (2, b'Izquierdo')], null=True)),
                ('escalon_mesial', models.IntegerField(blank=True, choices=[(1, b'Derecho'), (2, b'Izquierdo')], null=True)),
                ('escalon_distal', models.IntegerField(blank=True, choices=[(1, b'Derecho'), (2, b'Izquierdo')], null=True)),
                ('observaciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sobremordidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horizontal', models.IntegerField(choices=[(-20, b'-20'), (-19, b'-19'), (-18, b'-18'), (-17, b'-17'), (-16, b'-16'), (-15, b'-15'), (-14, b'-14'), (-13, b'-13'), (-12, b'-12'), (-11, b'-11'), (-10, b'-10'), (-9, b'-9'), (-8, b'-8'), (-7, b'-7'), (-6, b'-6'), (-5, b'-5'), (-4, b'-4'), (-3, b'-3'), (-2, b'-2'), (-1, b'-1'), (0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20')])),
                ('vertical', models.IntegerField(choices=[(-20, b'-20'), (-19, b'-19'), (-18, b'-18'), (-17, b'-17'), (-16, b'-16'), (-15, b'-15'), (-14, b'-14'), (-13, b'-13'), (-12, b'-12'), (-11, b'-11'), (-10, b'-10'), (-9, b'-9'), (-8, b'-8'), (-7, b'-7'), (-6, b'-6'), (-5, b'-5'), (-4, b'-4'), (-3, b'-3'), (-2, b'-2'), (-1, b'-1'), (0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20')])),
            ],
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_denticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
