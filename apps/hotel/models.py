# -*- coding: utf-8 -*-
from django.db import models
from apps.perfiles.models import Huesped


class Habitacion(models.Model):
    tip = (
        ('mds', 'mds'),
        ('mdt', 'mdt'),
        ('mdd', 'mdd'),
        )
    numero=models.CharField(max_length=5, unique=True)
    tipo=models.CharField(choices=tip, max_length=5,blank=True,verbose_name='Tipo')
    descripcion=models.TextField()

    def __str__(self):
        return self.numero
    
class Registro(models.Model):
    form = (
        ('E', 'Efectivo'),
        ('T', 'Tarjeta'),
        )
    fec_ingreso=models.DateTimeField()
    huesped=models.ForeignKey(Huesped)
    habitacion=models.ForeignKey(Habitacion)
    fec_salida=models.DateTimeField()
    tarifa=models.CharField(max_length=6)
    forma_pago=models.CharField(choices=form, max_length=1)

    def __str__(self):
        return '%s %s | %s' % (self.huesped.nombre, self.huesped.apellidos, self.habitacion.numero)
