from django.db import models
# from django.utils import timezone
from .Empresa import Empresa


class Huesped(models.Model):
    SEX = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )

    empresa = models.ForeignKey(Empresa)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    dni = models.CharField(max_length=8)
    sexo = models.CharField(choices=SEX, max_length=10,
                            blank=True, default='masculino')
    telefono = models.CharField(max_length=13)
    nacionalidad = models.CharField(max_length=40)
    procedencia = models.CharField(max_length=40)
    # fecha_nac = models.DateField(verbose_name='Fecha de Nacimiento')

    class Meta:
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"

    def __str__(self):
        return '%s - %s, %s' % (self.dni, self.apellidos, self.nombre)
