from django.contrib import admin
from .models import Familias, Personas, Ayudas_econ, Proyect, Categoria, Prestaciones, Producto, Traking_Prestaciones, TrackingAyudas
# Register your models here.

admin.site.register(Proyect)
admin.site.register(Familias)
admin.site.register(Personas)
admin.site.register(Ayudas_econ)
admin.site.register(Categoria)
admin.site.register(Prestaciones)
admin.site.register(Producto)
admin.site.register(Traking_Prestaciones)
admin.site.register(TrackingAyudas)