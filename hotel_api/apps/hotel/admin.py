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

admin.site.register(Consumo)
admin.site.register(Detalle)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Factura)
admin.site.register(Habitacion)
admin.site.register(Huesped)
admin.site.register(Producto)
admin.site.register(Sucursal)
