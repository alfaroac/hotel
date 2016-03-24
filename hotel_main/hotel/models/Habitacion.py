# -*- coding: utf-8 -*-
from django.db import models


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
    tipo = models.CharField(choices=tip, max_length=3, default='swb')
    descripcion = models.TextField()
    estado = models.CharField(
        choices=est, max_length=10, blank=True, default='libre')

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s  | %s' % (self.numero, self.tipo)
