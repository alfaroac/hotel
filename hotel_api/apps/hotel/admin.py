from django.contrib import admin
from .models.Consumo import Consumo
from .models.Detalle import Detalle
from .models.Empleado import Empleado
from .models.Empresa import Empresa
from .models.Factura import Factura
from .models.Habitacion import Habitacion
from .models.Huesped import Huesped
from .models.Producto import Producto
from .models.Sucursal import Sucursal


# class RegistroAdmin(admin.ModelAdmin):
#     list_display = ("huesped", "habitacion", "empresa")
#     search_fields = ("huesped", "habitacion",)
#     list_per_page = 2

# admin.site.register(Registro, RegistroAdmin)

admin.site.register(Consumo)
admin.site.register(Detalle)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Factura)
admin.site.register(Habitacion)
admin.site.register(Huesped)
admin.site.register(Producto)
admin.site.register(Sucursal)
