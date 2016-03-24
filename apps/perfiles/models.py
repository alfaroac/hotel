# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
    rol = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.rol


class Persona(models.Model):
    SEX = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )

    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    dni = models.CharField(max_length=8)
    fecha_nac = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(choices=SEX, max_length=10,
                            blank=True, default='masculino')
    telefono = models.CharField(max_length=13)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellidos, self.dni)


class Personal(models.Model):

    usuario = models.OneToOneField(User)
    persona = models.ForeignKey(Persona)
    rol = models.ForeignKey(Rol)
    direccion = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personales"

    def __str__(self):
        return self.usuario.username


class Huesped(models.Model):

    persona = models.ForeignKey(Persona)
    nacionalidad = models.CharField(max_length=40)
    procedencia = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"

    def __str__(self):
        return '%s %s' % (self.persona.nombre, self.persona.apellidos)
