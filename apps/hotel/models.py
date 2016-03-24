# -*- coding: utf-8 -*-
from django.db import models
from apps.perfiles.models import Huesped


class Habitacion(models.Model):
    tip = (
        ('swb', 'Habitación Simple'),
        ('dwb', 'Habitación doble'),
        ('mat', 'Habitación triple/departamento'),
    )
    est = (
        ('libre', 'Libre'),
        ('reservado', 'Reservado'),
        ('ocupado', 'Ocupado'),
        ('limpiar', 'limpiar'),
    )
    numero = models.CharField(max_length=5, unique=True)
    piso = models.CharField(max_length=4)
    tipo = models.CharField(choices=tip, max_length=5,
                            blank=True, verbose_name='Tipo', default='swb')
    descripcion = models.TextField()
    estado = models.CharField(
        choices=est, max_length=10, blank=True, default='libre')

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s  | %s' % (self.numero, self.tipo)


class Empresa(models.Model):

    razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=11)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.razon_social


class Registro(models.Model):
    form_p = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
    )
    fec_registro = models.DateTimeField(auto_now_add=True)
    fec_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    huesped = models.ForeignKey(Huesped)
    empresa = models.ForeignKey(Empresa, null=True)
    habitacion = models.ForeignKey(Habitacion)
    fec_salida = models.DateField()
    hora_salida = models.TimeField()
    forma_pago = models.CharField(
        choices=form_p, max_length=10, default='efectivo')
    tarifa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return '%s' % (self.huesped)


class Reserva(models.Model):
    tipo_hab = (
        ('swb', 'Habitación Simple'),
        ('dwb', 'Habitación doble'),
        ('mat', 'Habitación triple/departamento'),
    )
    fecha_reserva = models.DateTimeField(auto_now=True)
    habitacion = models.ForeignKey(Habitacion)
    tipo_habitacion = models.CharField(
        choices=tipo_hab, max_length=5, blank=True, default='swb')
    huesped = models.ForeignKey(Huesped)
    empresa = models.ForeignKey(Empresa)
    fecha_llegada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    observacion = models.TextField()

    def __str__(self):
        return '%s : %s' % (self.habitacion.numero, self.huesped)
