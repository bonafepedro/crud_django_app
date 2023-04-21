from django.db import models
from django.contrib.auth.models import User 
#from django.contrib.auth import get_current_user
from django.utils import timezone

ESTADO_CIVIL_CHOICES = [
                        ('S', 'Soltero/a'),
                        ('C', 'Casado/a'),
                        ('D', 'Divorciado/a'),
                        ('V', 'Viudo/a')
                        ]

CATEGORIAS_PRESTACIONES = [
    ('M', 'MODULO ALIMENTARIO'),
    ('C', 'CHAPA'),
    ('E', 'MEDICAMENTOS')
]

ESTADOS_SOLICITUD = [
    ('SOLICITADO', 'SOLICITADO'),
    ('APROBADO', 'APROBADO'),
    ('ENTREGADO', 'ENTREGADO')
]



# Create your models here.
""" 
def obtener_usuario_actual():
    return User.objects.get(pk=request.user.pk)
 """

class Proyect(models.Model):

    programas = models.CharField(max_length= 250)
    area = models.CharField(max_length= 20)
    usuario_creador = models.ForeignKey(User, 
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name='programa_creado')
    
    def __str__(self):
        return "{}".format(self.programas)

class Familias(models.Model):

    apellido = models.CharField(max_length=11)
    direccion = models.CharField(max_length= 50)
    cantidad = models.IntegerField()
    usuario_creador = models.ForeignKey(User, 
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name='familias_creadas')
    

    def __str__(self):
        #apellidoynombre = self.nombre + self.apellido
        return "{}".format(self.apellido)


class Personas(models.Model):

    nombre = models.CharField(max_length=11, default= "no especificado", blank=True)
    apellido = models.CharField(max_length=12, default= "no especificado", blank=True)

    grupo_familiar = models.ForeignKey(Familias, on_delete= models.CASCADE)
    cuil = models.CharField(max_length=11)
    genero = models.CharField(max_length= 20)
    estado_civil = models.CharField(max_length= 1, choices=ESTADO_CIVIL_CHOICES)
    profesion = models.CharField(max_length= 20)
    Direccion = models.CharField(max_length= 50)
    Barrio = models.CharField(max_length= 20)
    discapacidad = models.BooleanField()

    usuario_creador = models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name='personas_creadas')

    def __str__(self):
        #apellidoynombre = self.nombre + self.apellido
        return "{} {} {}".format(self.nombre, self.apellido, self.cuil)

class Ayudas_econ(models.Model):
    id_programa = models.ForeignKey(Proyect, on_delete= models.CASCADE,  default=1)
    id_beneficiario = models.ForeignKey(Personas, on_delete= models.CASCADE)
    monto = models.IntegerField()
    fecha = models.DateField(default=timezone.now)
    estado = models.CharField(max_length= 15, choices=ESTADOS_SOLICITUD, default= 'SOLICITADO')
    motivo = models.CharField(max_length= 20,
                              null=True,
                              blank=True,
                              default= 'emergencia')

    usuario_creador = models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'ayudas_economicas')
    



    def __str__(self):
        #apellidoynombre = self.nombre + self.apellido
        return "beneficiario: {}, monto: {}".format(self.id_beneficiario, self.monto)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)



class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    cantidad_usada = models.IntegerField(default=0)
    cantidad_deposito = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.nombre)

class Prestaciones(models.Model):
    id_programa = models.ForeignKey(Proyect, on_delete= models.CASCADE,  default=2)
    id_beneficiario = models.ForeignKey(Personas, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=15, choices= ESTADOS_SOLICITUD, default= 'SOLICITADO')
    fecha_solicitud = models.DateField(default=timezone.now)
    motivo = models.CharField(max_length= 20,
                              null=True,
                              blank=True,
                              default= 'emergencia')

    usuario_creador = models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'prestaciones')
    

    def __str__(self):
        #apellidoynombre = self.nombre + self.apellido
        return "beneficiario: {}, producto: {}, cantidad: {}".format(self.id_beneficiario, self.producto, self.cantidad)

class Traking_Prestaciones(models.Model):
    id_prestacion = models.ForeignKey(Prestaciones, on_delete= models.CASCADE)
    fecha_solicitud = models.DateField(null= True, blank= True)
    usuario_solicitud = models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'solicitud')
    fecha_aprobacion= models.DateField(null= True, blank= True)
    usuario_aprobacion= models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'aprobacion')
    fecha_entrega= models.DateField(null= True, blank= True)
    usuario_entrega= models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'entrega')
    lugar_entrega= models.CharField(max_length=20, blank= True, null= True)

class TrackingAyudas(models.Model):
    # campos de TrackingEntregas
    ayuda = models.ForeignKey(Ayudas_econ, on_delete=models.CASCADE)
    fecha_solicitud_ay = models.DateField(null= True, blank= True)
    usuario_solicitud = models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'usuario_solicitud_ay')
    fecha_aprobacion_ay= models.DateField(null= True, blank= True)
    usuario_aprobacion= models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'usuario_aprobacion_ay')
    fecha_entrega_ay= models.DateField(null= True, blank= True)
    usuario_entrega= models.ForeignKey(User,
                                        on_delete= models.SET("usuario eliminado"),
                                        null=True,
                                        blank=True,
                                        related_name= 'usuario_entrega_ay')
    lugar_entrega= models.CharField(max_length=20, blank= True, null= True)

