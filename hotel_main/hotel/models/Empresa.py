from django.db import models


class Empresa(models.Model):

    razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=11)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.razon_social
