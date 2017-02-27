# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-26 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenciaLabial',
            fields=[
                ('id_competenciaLabial', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipo_competenciaLabial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FacialFrontal',
            fields=[
                ('id_frontal_facial', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('frontal_facial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilTotal',
            fields=[
                ('id_tipoPerfiltotal', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipoPerfiltotal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PTercioInferioir',
            fields=[
                ('id_perfilTercio_inferior', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('perfilTercio_inferior', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sonrisa',
            fields=[
                ('id_tipoSonrisa', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipoSonrisa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoNariz', models.CharField(max_length=25)),
                ('angulo_Naso_labial', models.IntegerField()),
                ('tercio_superior', models.IntegerField()),
                ('tercio_medio', models.IntegerField()),
                ('tercio_inferior', models.IntegerField()),
                ('tamanoSonrisa', models.IntegerField()),
                ('grosorLabios', models.IntegerField()),
                ('tamanoLabios', models.IntegerField()),
                ('fichas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas')),
                ('frontal_facial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.FacialFrontal')),
                ('perfilTercio_inferior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.PTercioInferioir')),
                ('tipoPerfiltotal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.PerfilTotal')),
                ('tipoSonrisa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.Sonrisa')),
                ('tipo_competenciaLabial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.CompetenciaLabial')),
            ],
        ),
    ]
