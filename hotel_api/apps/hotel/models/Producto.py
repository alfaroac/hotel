from django.db import models


class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
