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
    estado = models.CharField(choices=est, max_length=10, blank=True, default='libre')

    def __str__(self):
        return '%s | %s' % (self.numero, self.tipo)


class Registro(models.Model):
    form_p = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
    )

    fec_ingreso = models.DateTimeField()
    huesped = models.ForeignKey(Huesped)
    habitacion = models.ForeignKey(Habitacion)
    fec_salida = models.DateTimeField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forma_pago = models.CharField(choices=form_p, max_length=10, default='efectivo')

    def __str__(self):
        return '%s %s | %s' % (self.huesped.nombre, self.huesped.apellidos, self.habitacion.numero)
