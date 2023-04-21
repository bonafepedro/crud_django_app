from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Prestaciones, Producto, Traking_Prestaciones, Ayudas_econ, TrackingAyudas
from django.utils import timezone
from django.contrib.auth.models import User



@receiver(post_save, sender=Prestaciones)
def actualizar_cantidad_usada(sender, instance, created, **kwargs):
    if created:
        id_producto = instance.producto.id
        print(id_producto)
        producto = Producto.objects.get(id = id_producto)

        if producto:
            producto.cantidad_usada += instance.cantidad
            producto.cantidad_deposito -= instance.cantidad
            producto.save()




@receiver(post_save, sender=Prestaciones)
def crear_tracking_entrega(sender, instance, created, **kwargs):
    if created:
        # crear una nueva instancia en TrackingEntregas
        tracking_entrega = Traking_Prestaciones(id_prestacion=instance)
        tracking_entrega.usuario_solicitud= instance.usuario_creador
        tracking_entrega.fecha_solicitud = timezone.now()
        tracking_entrega.save()
    elif instance.estado == "APROBADO":
        # crear una instancia adicional en TrackingEntregas
        tracking_aprobacion = Traking_Prestaciones.objects.get(id_prestacion=instance)
        tracking_aprobacion.usuario_aprobacion=instance.usuario_creador
        tracking_aprobacion.fecha_aprobacion = timezone.now()
        tracking_aprobacion.save()

    elif instance.estado == "ENTREGADO":
        tracking_entregado = Traking_Prestaciones.objects.get(id_prestacion=instance)
        tracking_entregado.usuario_entrega=instance.usuario_creador
        tracking_entregado.fecha_entrega = timezone.now()
        tracking_entregado.save()


@receiver(post_save, sender=Ayudas_econ)
def crear_tracking_ayudas(sender, instance, created, **kwargs):
    if created:
        # crear una nueva instancia en TrackingEntregas
        tracking_entrega = TrackingAyudas(ayuda=instance)
        tracking_entrega.usuario_solicitud= instance.usuario_creador
        tracking_entrega.fecha_solicitud_ay = timezone.now()
        tracking_entrega.save()
    elif instance.estado == "APROBADO":
        # crear una instancia adicional en TrackingEntregas
        tracking_aprobacion = TrackingAyudas.objects.get(ayuda=instance)
        tracking_aprobacion.usuario_aprobacion=instance.usuario_creador
        tracking_aprobacion.fecha_aprobacion_ay = timezone.now()
        tracking_aprobacion.save()

    elif instance.estado == "ENTREGADO":
        tracking_entregado = TrackingAyudas.objects.get(ayuda=instance)
        tracking_entregado.usuario_entrega=instance.usuario_creador
        tracking_entregado.fecha_entrega_ay = timezone.now()
        tracking_entregado.save()

