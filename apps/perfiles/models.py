# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
    rol = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.rol


class Personal(models.Model):
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    usuario = models.OneToOneField(User)
    dni = models.CharField(max_length=8)
    rol = models.ForeignKey(Rol)
    sexo = models.CharField(choices=SEX, max_length=255,
                            blank=True, verbose_name='Género')
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=13)
    imagen = models.ImageField(upload_to='perfiles')

    def __str__(self):
        return self.usuario.username


class Huesped(models.Model):
    SEX = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )

    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    dni = models.CharField(max_length=8)
    fecha_nac = models.DateTimeField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(choices=SEX, max_length=10,
                            blank=True, default='masculino')
    telefono = models.CharField(max_length=13)
    nacionalidad = models.CharField(max_length=40)
    procedencia = models.CharField(max_length=40)
    # imagen = models.ImageField(upload_to='perfiles')

    def __str__(self):
        return '%s %s |%s' % (self.nombre, self.apellidos, self.dni)
    
