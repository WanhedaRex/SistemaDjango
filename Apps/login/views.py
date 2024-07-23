from django.shortcuts import render, redirect
from .models import Registro
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Provee


# Create your views here.

def home (request):
    return render (request, "login.html")
def registro_view(request):
    return render(request,'registro.html')
def login_view(request):
    return render(request,'login.html')
def sistema_view(request):
    return render(request,'sistema.html')
def ordenCompleta_view(request):
    return render(request,'ordenCompleta.html')
def base_view(request):
    return render(request,'base.html')
def extends_view(request):
    return render(request,'extends.html')
def empleado_view(request):
    return render(request,'empleado.html')
def gerente_view(request):
    return render(request,'gerente.html')
def proveedores_view(request):
    return render(request,'proveedores.html')
def gestionProveedores_view(request):
    return render(request,'gestionProveedores.html')
def edicionProveedores_view (request):
    return render(request,'edicionProveedores.html')
def ver_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ordenCompleta.html', {'ticket': ticket})

def RegistroUsuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombreUsuario')
        correo_electronico = request.POST.get('correoElectronico')
        password = request.POST.get('password')
        nuevo_registro = Registro(nombreUsuario=nombre_usuario,correoElectronico=correo_electronico,password=password)
        nuevo_registro.save()
        return redirect('login')
    else:
         return render(request, 'registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.error(request, 'Credenciales no válidas')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def RegistroProveedores(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre_Proveedor = request.POST.get('nombreProveedor')
        numero = request.POST.get('numero')
        nuevo_proveedor = Provee(codigo=codigo,nombreProveedor=nombre_Proveedor,numero=numero)
        nuevo_proveedor.save()
        return redirect('login')
    else:
         return render(request, 'proveedores.html')

def casa(request):
    proveedoresListados = Provee.objects.all()
    messages.success(request, '¡Proveedores listados!')
    return render(request, 'gestionProveedores.html', {"proveedores": proveedoresListados})

def registrarProveedores(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['nombre']
    numero = request.POST['numero']

    proveedoresListados = Provee.objects.create(
    codigo=codigo, nombre=nombre, numero=numero)
    messages.success(request, '¡Proveedor registrado!')
    return redirect('/')


def edicionProveedores(request, codigo):
    proveedoresListados = Provee.objects.get(codigo=codigo)
    return render(request, 'edicionProveedores.html', {"proveedores": proveedoresListados})


def editarProveedores(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['nombre']
    numero = request.POST['numero']

    proveedoresListados = Provee.objects.get(codigo=codigo)
    proveedoresListados.nombre = nombre
    proveedoresListados.numero = numero
    proveedoresListados.save()

    messages.success(request, '¡Proveedor actualizado!')

    return redirect('/')


def eliminarProveedores(request, codigo):
    proveedoresListados = Provee.objects.get(codigo=codigo)
    proveedoresListados.delete()

    messages.success(request, '¡Proveedor eliminado!')

    return redirect('/')