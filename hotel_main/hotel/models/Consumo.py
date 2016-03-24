from django.db import models
from .Producto import Producto


class Consumo(models.Model):

    producto = models.ForeignKey(Producto)
    reserva = models.ForeignKey()
    cantidad = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Consumo"
        verbose_name_plural = "Consumos"

    def __str__(self):
        return self.producto
