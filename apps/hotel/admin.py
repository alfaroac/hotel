from django.contrib import admin
from models import Habitacion, Empresa, Registro, Reserva


class RegistroAdmin(admin.ModelAdmin):
    list_display = ("huesped", "habitacion", "empresa")
    search_fields = ("huesped", "habitacion",)
    list_per_page = 2

admin.site.register(Habitacion)
admin.site.register(Empresa)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Reserva)
