from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, JsonResponse
from .models import Familias, Personas, Proyect, Ayudas_econ, Prestaciones
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import Crear_Persona, Crear_Familia, Crear_AyEc, Crear_Programa, Crear_Prestacion
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
# Create your views here.


def home(request):
    return render(request, 'home.html')


# Bloque signin signup signout

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',
                      {
                          "form": UserCreationForm
                      })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect(home)

            except IntegrityError:
                # return HttpResponse('El usuario ya existe')
                return render(request, 'signup.html',
                              {"form": UserCreationForm,
                               'error': 'El usuario ya existe'
                               })
        # return HttpResponse('Las contraseñas no coinciden')

        return render(request, 'signup.html',
                      {
                          "form": UserCreationForm,
                          'error': 'Las contraseñas no coinciden'
                      })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html',
                      {
                          "form": AuthenticationForm
                      })

    else:
        print(request.POST)
        usuario = authenticate(request,
                               username=request.POST['username'],
                               password=request.POST['password']
                               )

        if usuario is None:

            return render(request, 'signin.html',
                          {
                              'form': AuthenticationForm,
                              'error': "El usuario o contraseña son incorrectos"
                          })
        else:
            login(request, usuario)
            return redirect(home)


# Bloque personas

@login_required
def listado_personas(request):

    personas = Personas.objects.filter(usuario_creador=request.user)
    return render(request,
                  'personas.html',
                  {
                      'personas': personas
                  })


@login_required
def agregar_personas(request):

    if request.method == 'GET':
        return render(request, 'agregar_persona.html',
                      {
                          'form': Crear_Persona
                      })
    else:

        try:
            form = Crear_Persona(request.POST)
            nueva_persona = form.save(commit=False)
            print(nueva_persona)
            nueva_persona.usuario_creador = request.user
            nueva_persona.save()

            return redirect('home')

        except ValueError:
            return render(request, 'agregar_persona.html',
                          {
                              'form': Crear_Persona,
                              'error': 'Datos Erróneos'
                          })


def update_person(request, person_id):

    if request.method == 'GET':

        persona = get_object_or_404(
            Personas, id=person_id, usuario_creador=request.user)
        form = Crear_Persona(instance=persona)

        return render(request, 'detalle_personas.html',
                      {
                          'persona': persona,
                          'form': form
                      })

    else:
        try:

            persona = get_object_or_404(
                Personas, id=person_id, usuario_creador=request.user)
            form = Crear_Persona(request.POST, instance=persona)
            form.save()

            return redirect('listado_personas')

        except ValueError:
            return render(request, 'detalle_personas.html',
                          {
                              'persona': persona,
                              'form': form,
                              'error': 'Error actualizando datos'
                          })

# Bloque familias


@login_required
def agregar_familias(request):

    if request.method == 'GET':
        return render(request, 'agregar_familia.html',
                      {
                          'form': Crear_Familia
                      })
    else:

        try:
            form = Crear_Familia(request.POST)
            nueva_familia = form.save(commit=False)
            print(nueva_familia)
            nueva_familia.usuario_creador = request.user
            nueva_familia.save()

            return redirect('home')

        except ValueError:
            return render(request, 'agregar_familia.html',
                          {
                              'form': Crear_Familia,
                              'error': 'Datos Erróneos'
                          })


@login_required
def listado_familias(request):

    familias = Familias.objects.filter(usuario_creador=request.user)
    return render(request,
                  'familias.html',
                  {
                      'familias': familias
                  })


"""

def familias(request):
    #familia = get_object_or_404(Familias, id = id)
    #return HttpResponse("familia: %s" % familia.direccion)

    familia = list(Familias.objects.values())
    return JsonResponse(familia, safe= False)

"""
# Bloque Programas


def listar_programas(request):

    programas = Proyect.objects.filter(usuario_creador=request.user)
    return render(request,
                  'programas.html',
                  {
                      'programas': programas
                  })


def actualizar_programas(request, program_id):
    if request.method == 'GET':

        programa = get_object_or_404(
            Proyect, id=program_id, usuario_creador=request.user)
        form = Crear_Programa(instance=programa)

        return render(request, 'detalle_programas.html',
                      {
                          'programa': programa,
                          'form': form
                      })

    else:
        try:

            programa = get_object_or_404(
                Proyect, id=program_id, usuario_creador=request.user)
            form = Crear_Programa(request.POST, instance=programa)
            form.save()

            return redirect('listado_programas')

        except ValueError:
            return render(request, 'detalle_programas.html',
                          {
                              'programa': programa,
                              'form': form,
                              'error': 'Error actualizando datos'
                          })


# Ayudas Económicas

@login_required
def agregar_ayuda_economica(request):

    if request.method == 'GET':
        return render(request, 'agregar_ayudaeconomica.html',
                      {
                          'form': Crear_AyEc
                      })
    else:

        try:
            form = Crear_AyEc(request.POST)
            nueva_ayuda = form.save(commit=False)
            print(nueva_ayuda)
            nueva_ayuda.usuario_creador = request.user
            nueva_ayuda.save()

            return redirect('home')

        except ValueError:
            return render(request, 'agregar_ayudaeconomica.html',
                          {
                              'form': Crear_AyEc,
                              'error': 'Datos Erróneos'
                          })

@login_required
def listar_ayuda_economica(request):

    ayudas = Ayudas_econ.objects.filter(usuario_creador=request.user)
    return render(request,
                  'ayudas_economicas.html',
                  {
                      'ayudas': ayudas
                  })

@login_required
def actualizar_ayuda_economica(request, ayuda_id):
    if request.method == 'GET':

        ayuda = get_object_or_404(
            Ayudas_econ, id=ayuda_id, usuario_creador=request.user)
        form = Crear_AyEc(instance=ayuda)

        return render(request, 'detalle_ayudas.html',
                      {
                          'ayudas': ayuda,
                          'form': form
                      })

    else:
        try:

            ayuda = get_object_or_404(
                Ayudas_econ, id=ayuda_id, usuario_creador=request.user)
            form = Crear_AyEc(request.POST, instance=ayuda)
            form.save()

            return redirect('listado_ayudas')

        except ValueError:

            return render(request,
                          'detalle_ayudas.html', {
                              'ayudas': ayuda,
                              'form': form,
                              'error': 'Error actualizando datos'
                          })


# Prestaciones

@login_required
def agregar_prestacion(request):

    if request.method == 'GET':
        return render(request, 'agregar_prestacion.html',
                      {
                          'form': Crear_Prestacion
                      })
    else:

        try:
            form = Crear_Prestacion(request.POST)
            nueva_prestacion = form.save(commit=False)
            print(nueva_prestacion)
            nueva_prestacion.usuario_creador = request.user
            nueva_prestacion.save()

            return redirect('home')

        except ValueError:
            return render(request, 'agregar_prestacion.html',
                          {
                              'form': Crear_Prestacion,
                              'error': 'Datos Erróneos'
                          })

@login_required
def listar_prestaciones(request):

    prestaciones = Prestaciones.objects.filter(usuario_creador=request.user)
    return render(request,
                  'prestaciones.html',
                  {
                      'prestaciones': prestaciones
                  })


@login_required
def actualizar_prestacion(request, prestacion_id):
    if request.method == 'GET':

        prestacion = get_object_or_404(
            Prestaciones, id=prestacion_id, usuario_creador=request.user)
        form = Crear_Prestacion(instance=prestacion)

        return render(request, 'detalle_prestaciones.html',
                      {
                          'prestaciones': prestacion,
                          'form': form
                      })

    else:
        try:

            prestacion = get_object_or_404(
                Prestaciones, id=prestacion_id, usuario_creador=request.user)
            form = Crear_Prestacion(request.POST, instance=prestacion)
            form.save()

            return redirect('listado_prestaciones')

        except ValueError:

            return render(request,
                          'detalle_prestaciones.html', {
                              'prestaciones': prestacion,
                              'form': form,
                              'error': 'Error actualizando datos'
                          })

