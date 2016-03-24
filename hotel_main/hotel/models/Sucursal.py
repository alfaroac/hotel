from django.db import models


class Sucursal(models.Model):

    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.razon_social
