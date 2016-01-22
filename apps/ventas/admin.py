from django.contrib import admin
from models import Consumo, Detalle


class ConsumoAdmin(admin.ModelAdmin):
    list_display = ("pax", "descripcion", "cantidad", "fecha")
    search_fields = ("pax", "descripcion")
    list_per_page = 2


class DetalleAdmin(admin.ModelAdmin):
    list_display = ("huesped", "descripcion", "total")
    search_fields = ("huesped", "descripcion")
    list_per_page = 2


admin.site.register(Consumo, ConsumoAdmin)
admin.site.register(Detalle, DetalleAdmin)
