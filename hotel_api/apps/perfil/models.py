# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class TipoUsuario(models.Model):

    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "TipoUsuario"
        verbose_name_plural = "TipoUsuarios"

    def __str__(self):
        return "%s" % (self.tipo)


class Perfil(models.Model):
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    usuario = models.OneToOneField(User)
    telefono = models.IntegerField(null=True, blank= True)
    dni = models.CharField(max_length=8, null = True, blank = True)
    rol = models.ForeignKey(TipoUsuario, null= True, blank =True)
    sexo = models.CharField(choices=SEX, max_length=20, null=True,
                            blank=True, verbose_name='Género')
    direccion = models.CharField(max_length=150, null= True, blank=True)
    celular = models.CharField(max_length=13, null=True, blank = True)
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='perfiles', null=True, blank=True)

    def __str__(self):
        return " %s %s %s"% (self.usuario.first_name, self.usuario.last_name, self.dni)
# Create your models here.
