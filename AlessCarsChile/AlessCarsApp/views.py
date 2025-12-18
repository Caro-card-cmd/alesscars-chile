from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   #login_required, decorador que obliga a logearse a la vista reserva
from django.contrib.auth import logout                      #logout, libreria que permite salir de la sesion iniciada.
#django.contrib.auth --> librerias de django
from .models import agenda
from .form import agendaForm
from django.contrib import messages  # para mostrar alertas
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

#PROCESO DE LOGEO
def index(req):   #mi base.html
    return render(req,'index.html')

def registro(req):
    if req.method == 'POST':   #verificar los datos que llegan del formulario
        usuario = req.POST.get('usuario')
        correo = req.POST.get('correo')
        telefono = req.POST.get('telefono')
        clave = req.POST.get('clave')
        tipo = req.POST.get('tipo')
        if User.objects.filter(username=usuario).exists():
            messages.error(req, "El usuario ya existe")
            return render(req, 'templateslogear/registro.html')
        user = User.objects.create_user(
            username=usuario,
            email=correo,
            password=clave)
        user.save()
        messages.success(req, "Registro exitoso")
        return redirect("logear")
    return render(req, "templateslogear/registro.html")

def logear(req):
    if req.method == 'POST':
        usuario = req.POST.get('usuario')
        clave = req.POST.get('clave')
        user = authenticate(req, username=usuario, password=clave)
        if user:
            login(req, user)
            return redirect('gestion')
        else:
            messages.error(req, "Usuario o contraseña incorrectos.")
            return render(req, 'templateslogear/logear.html')
    return render(req, 'templateslogear/logear.html')

def exit(req):
    logout(req)  #logout, libreria que permite salir de la sesion
    return redirect('index')

# INGRESAR INDEX DE PAGINAS:
@login_required
def gestion(req):
    servicios = agenda.objects.all()
    return render(req, 'templatesbase/gestion.html', {'servicios': servicios})

def enviar_confirmacion(req):
    return render(req, "templatesbase/gracias.html")

def nosotros(req):
    return render(req,'templatesbase/nosotros.html')

def gracias(req):
    return render(req,'templatesbase/gracias.html')

def servicios(req):
    return render(req,'templatesbase/servicios.html')

# CRUD:
@login_required
def crear_servicio(req):
    formulario = agendaForm(req.POST or None, req.FILES or None)  #req. POST: contiene datos, or None: si no hay datos, muestra archivo vacio, req.FILES: archivos enviados 'imagenes'
    if formulario.is_valid():
        formulario.save()
        return redirect('gestion')
    return render(req, 'templatesbase/crear_servicio.html', {'formulario': formulario})  #se debe mostrar la pagina de Crear_servicios y enviar datos, como la variable formulario

@login_required
def editar_servicio(req, id):
    servicio = agenda.objects.get(id=id)
    formulario = agendaForm(req.POST or None, req.FILES or None, instance=servicio)
    if formulario.is_valid():
        formulario.save()
        return redirect('gestion')
    return render(req, 'templatesbase/editar_servicio.html', {'formulario': formulario})

@login_required
def eliminar(req, id):
    servicio = agenda.objects.get(id=id)
    servicio.delete()
    return redirect('gestion')
    