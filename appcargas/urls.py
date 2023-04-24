from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    #path("pepito/", views.pepito),
    #path("familias/", views.familias),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name='signout'),
    path("signin/", views.signin, name= 'signin'),
    path("personas/", views.listado_personas, name= 'listado_personas'),
    path("personas/agregar/", views.agregar_personas, name= "agregar_personas"),
    path("personas/<int:person_id>/", views.update_person, name= "actualizar_personas"),
    path("personas/<int:person_id>/delete/", views.delete_person, name= "eliminar_personas"),
    path("familias/", views.listado_familias, name= 'listado_familias'),
    path("familias/agregar/", views.agregar_familias, name= "agregar_familias"),
    path("programas/", views.listar_programas, name= 'listado_programas'),
    path("programas/<int:program_id>", views.actualizar_programas, name= 'actualizar_programas'),
    path("ayudas/", views.listar_ayuda_economica, name= 'listado_ayudas'),
    path("ayudas/agregar/", views.agregar_ayuda_economica, name= "agregar_ayudaec"),
    path("ayudas/<int:ayuda_id>", views.actualizar_ayuda_economica, name= 'actualizar_ayudas'),
    path("prestaciones/", views.listar_prestaciones, name= 'listado_prestaciones'),
    path("prestaciones/agregar/", views.agregar_prestacion, name= "agregar_prestacion"),
    path("prestaciones/<int:prestacion_id>", views.actualizar_prestacion, name= 'actualizar_prestacion')

]