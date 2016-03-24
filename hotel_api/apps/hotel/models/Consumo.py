from django.db import models
from .Producto import Producto


class Consumo(models.Model):

    producto = models.ForeignKey(Producto)

    class Meta:
        verbose_name = "Consumo"
        verbose_name_plural = "Consumos"

    def __str__(self):
        return self.producto
