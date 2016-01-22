from django.contrib import admin
from models import Rol, Persona, Personal, Huesped


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "dni", "sexo")
    search_fields = ("apellidos", "dni")
    list_per_page = 2

admin.site.register(Rol)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Personal)
admin.site.register(Huesped)
