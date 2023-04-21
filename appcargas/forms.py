from django.forms import ModelForm
from .models import Personas, Familias, Ayudas_econ, Proyect, Prestaciones
from django_select2 import forms as s2forms




class Crear_Persona(ModelForm):
    class Meta:
        model = Personas
        fields = [
            'nombre',
            'apellido',
            'grupo_familiar',
            'cuil',
            'genero',
            'estado_civil',
            'profesion',
            'Direccion',
            'Barrio',
            'discapacidad'
        ]

        
class Crear_Familia(ModelForm):
    class Meta:
        model = Familias
        fields = [
            'apellido',
            'direccion',
            'cantidad'
        ]


# Programas

class Crear_Programa(ModelForm):
    class Meta:
        model = Proyect
        fields = [
            'programas',
            'area'
        ]

        
class Crear_AyEc(ModelForm):

    class Meta:
        model = Ayudas_econ
        fields = [
            'id_beneficiario',
            'monto',
            'fecha',
            'estado',
            'motivo'
        ]


class Crear_Prestacion(ModelForm):

    class Meta:
        model = Prestaciones
        fields = [
            'id_beneficiario',
            'categoria',
            'producto',
            'cantidad',
            'estado',
            'motivo'
        ]