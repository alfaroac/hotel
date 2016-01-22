# -*- coding: utf-8 -*-
from django.db import models
from apps.perfiles.models import Huesped


class Consumo(models.Model):

    fecha = models.DateTimeField(auto_now=True)
    pax = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    importe = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Consumo"
        verbose_name_plural = "Consumos"

    def __str__(self):
        return self.descripcion


class Detalle(models.Model):
    forma_p = (
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
    )

    huesped = models.ForeignKey(Huesped)
    descripcion = models.ForeignKey(Consumo)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forma_pago = models.CharField(
        choices=forma_p, max_length=8, blank=True, default='EFECTIVO')

    def __str__(self):
        return '%s ' % (self.descripcion)
