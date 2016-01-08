# -*- coding: utf-8 -*-
from django.db import models
from apps.perfiles.models import Huesped


class Habitacion(models.Model):
    tip = (
        ('swb', 'Habitación Simple/Matrimonial'),
        ('dwb', 'Habitación doble'),
        ('mat', 'Habitación triple/departamento'),
        )
    numero=models.CharField(max_length=5, unique=True)
    piso=models.CharField(max_length=4)
    tipo=models.CharField(choices=tip, max_length=5,blank=True,verbose_name='Tipo')
    descripcion=models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.numero
    
class Registro(models.Model):
    form = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        )
    fec_ingreso=models.DateTimeField()
    huesped=models.ForeignKey(Huesped)
    habitacion=models.ForeignKey(Habitacion)
    fec_salida=models.DateTimeField()
    tarifa=models.CharField(max_length=6, verbose_name='Costo alojamiento')
    forma_pago=models.CharField(choices=form, max_length=10)

    def __str__(self):
        return '%s %s | %s' % (self.huesped.nombre, self.huesped.apellidos, self.habitacion.numero)
