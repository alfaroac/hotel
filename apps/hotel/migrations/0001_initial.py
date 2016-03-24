# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-22 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=11)),
                ('direccion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5, unique=True)),
                ('piso', models.CharField(max_length=4)),
                ('tipo', models.CharField(blank=True, choices=[(b'swb', b'Habitaci\xc3\xb3n Simple'), (b'dwb', b'Habitaci\xc3\xb3n doble'), (b'mat', b'Habitaci\xc3\xb3n triple/departamento')], default=b'swb', max_length=5, verbose_name=b'Tipo')),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(blank=True, choices=[(b'libre', b'Libre'), (b'reservado', b'Reservado'), (b'ocupado', b'Ocupado'), (b'limpiar', b'limpiar')], default=b'libre', max_length=10)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_registro', models.DateTimeField(auto_now_add=True)),
                ('fec_ingreso', models.DateField()),
                ('hora_ingreso', models.TimeField()),
                ('fec_salida', models.DateField()),
                ('hora_salida', models.TimeField()),
                ('forma_pago', models.CharField(choices=[(b'efectivo', b'Efectivo'), (b'tarjeta', b'Tarjeta')], default=b'efectivo', max_length=10)),
                ('tarifa', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Empresa')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Habitacion')),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.Huesped')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField(auto_now=True)),
                ('tipo_habitacion', models.CharField(blank=True, choices=[(b'swb', b'Habitaci\xc3\xb3n Simple'), (b'dwb', b'Habitaci\xc3\xb3n doble'), (b'mat', b'Habitaci\xc3\xb3n triple/departamento')], default=b'swb', max_length=5)),
                ('fecha_llegada', models.DateTimeField()),
                ('fecha_salida', models.DateTimeField()),
                ('tarifa', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('observacion', models.TextField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Empresa')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Habitacion')),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.Huesped')),
            ],
        ),
    ]
