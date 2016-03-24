# -*- coding: utf-8 -*-
from django.db import models
# from django.utils import timezone
from .Sucursal import Sucursal
from django.contrib.auth.models import User


class Empleado(models.Model):
    rol_ = (
        ('admin', 'Admin'),
        ('secretario', 'Secretario'),
        ('recepcion', 'Recepción'),
    )
    usuario = models.OneToOneField(User)
    sucursal = models.ForeignKey(Sucursal)
    rol = models.CharField(choices=rol_, max_length=10, default='admin')
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.usuario
