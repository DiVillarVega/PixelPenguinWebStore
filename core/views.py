from django.shortcuts import render, redirect
from .zpoblar import poblar_bd
from .models import Producto

def index(request):
    productos = Producto.objects.all().order_by('nombre')
    data = { 'productos': productos }
    return render(request, 'core/index.html', data)

def ficha(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'core/ficha.html', { 'producto': producto })

def registro(request):
    return render(request, 'core/registro.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def productos(request, accion, id):
    return render(request, 'core/productos.html')

def usuarios(request, accion, id):
    return render(request, 'core/usuarios.html')

def bodega(request):
    return render(request, 'core/bodega.html')

def ventas(request):
    return render(request, 'core/ventas.html')

def boleta(request, nro_boleta):
    return render(request, 'core/boleta.html')

def ingresar(request):
    return render(request, 'core/ingresar.html')

def misdatos(request):
    return render(request, 'core/misdatos.html')

def miscompras(request):
    return render(request, 'core/miscompras.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def ropa(request):
    return render(request, 'core/ropa.html')

def poblar(request):
    # Permite poblar la base de datos con valores de prueba en todas sus tablas.
    # Opcionalmente se le puede enviar un correo único, para que los Administradores
    # del sistema puedan probar el cambio de password de los usuarios, en la página
    # de "Adminstración de usuarios".
    poblar_bd('j.perez@duocuc.cl')
    return redirect(index)