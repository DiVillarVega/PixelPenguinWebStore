from .zpoblar import poblar_bd
from .models import Producto

def index(request):
    productos = Producto.objects.all().order_by('nombre')
    data = { 'productos': productos }
    return render(request, 'core/index.html', data)

def ficha(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    data = { 'producto': producto }
    return render(request, 'core/index.html', data)

def poblar(request):
    # Permite poblar la base de datos con valores de prueba en todas sus tablas.
    # Opcionalmente se le puede enviar un correo único, para que los Administradores
    # del sistema puedan probar el cambio de password de los usuarios, en la página
    # de "Adminstración de usuarios".
    poblar_bd('j.perez@duocuc.cl')
    return redirect(index)