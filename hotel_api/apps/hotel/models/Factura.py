from django.db import models
# from django.utils import timezone
from .Empleado import Empleado
from .Huesped import Huesped
from .Detalle import Detalle


class Factura(models.Model):
    forma_p = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
    )
    empleado = models.ForeignKey(Empleado)
    huesped = models.ForeignKey(Huesped)
    detalle = models.ForeignKey(Detalle)
    forma_pago = models.CharField(
        choices=forma_p, max_length=10, default='admin')

    created_at = models.DateTimeField(
        auto_now_add=True)  # datetime.date.today()
    updated_at = models.DateTimeField(auto_now=True)  # datetime.date.today()

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return self.huesped
