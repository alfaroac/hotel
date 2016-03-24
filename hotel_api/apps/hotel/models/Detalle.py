from django.db import models
from .Habitacion import Habitacion
from .Consumo import Consumo


class Detalle(models.Model):

    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    habitacion = models.ForeignKey(Habitacion)
    consumo = models.ForeignKey(Consumo)

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"

    def __str__(self):
        return self.cantidad
