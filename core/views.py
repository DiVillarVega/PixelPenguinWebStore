from datetime import date
from django.shortcuts import render, redirect
from .zpoblar import poblar_bd
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.utils.safestring import SafeString
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto, Boleta, Carrito, DetalleBoleta, Bodega, Perfil
from .forms import ProductoForm, BodegaForm, IngresarForm, UsuarioForm, PerfilForm
from .forms import RegistroUsuarioForm, RegistroPerfilForm
from .templatetags.custom_filters import formatear_dinero, formatear_numero
from .tools import eliminar_registro, verificar_eliminar_registro, show_form_errors
from django.core.mail import send_mail

def es_personal_autenticado_y_activo(user):
    return (user.is_staff or user.is_superuser) and user.is_authenticated and user.is_active

def es_usuario_anonimo(user):
    return user.is_anonymous

def es_cliente_autenticado_y_activo(user):
    return (not user.is_staff and not user.is_superuser) and user.is_authenticated and user.is_active


def index(request):

    if request.method == 'POST':
            buscar = request.POST.get('buscar')
            registros = Producto.objects.filter(nombre__icontains=buscar).order_by('nombre')
        
    if request.method == 'GET':
            
            registros = Producto.objects.all().order_by('nombre')

    productos = []
    for registro in registros:
        productos.append(obtener_info_producto(registro.id))

        context = { 'productos': productos }
        
        return render(request, 'core/index.html', context)
    

def ficha(request, producto_id):
    context = obtener_info_producto(producto_id)
    return render(request, 'core/ficha.html', context)

def nosotros(request):
    return render(request, 'core/nosotros.html')


def ropa(request):
    return render(request, 'core/ropa.html')

@user_passes_test(es_usuario_anonimo, login_url='index')
def ingresar(request):

    if request.method == "POST":
        form = IngresarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'¡Bienvenido(a) {user.first_name} {user.last_name}!')
                    return redirect(index)
                else:
                    messages.error(request, 'La cuenta está desactivada.')
            else:
                messages.error(request, 'La cuenta o la password no son correctos')
        else:
            messages.error(request, 'No se pudo ingresar al sistema')
            show_form_errors(request, [form])

    if request.method == "GET":

        form = IngresarForm()

    context = {
        'form':  IngresarForm(),
        'perfiles': Perfil.objects.all().order_by('tipo_usuario', 'subscrito'),
    }

    return render(request, "core/index.html", context)

@login_required
def salir(request):
    nombre = request.user.first_name
    apellido = request.user.last_name
    messages.success(request, f'¡Hasta pronto {nombre} {apellido}!')
    logout(request)
    return redirect(index)


#INCOMPLETO***************************************************************************************************#

@user_passes_test(es_usuario_anonimo)
def registro(request):
    
    if request.method == 'POST':
        
        # CREAR: usar RegistroUsuarioForm para obtener datos del formulario
        # CREAR: usar RegistroPerfilForm para obtener datos del formulario
        # CREAR: lógica para crear usuario
        pass
    
    if request.method == 'GET':

        # CREAR: un formulario RegistroUsuarioForm vacío
        # CREAR: un formulario RegistroPerfilForm vacío
        pass

    # CREAR: variable de contexto para enviar formulario de usuario y perfil
    context = { }

    return render(request, 'core/registro.html', context)

@login_required
def misdatos(request):

    if request.method == 'POST':
        
        # CREAR: un formulario UsuarioForm para recuperar datos del formulario asociados al usuario actual
        # CREAR: un formulario RegistroPerfilForm para recuperar datos del formulario asociados al perfil del usuario actual
        # CREAR: lógica para actualizar los datos del usuario
        pass

    if request.method == 'GET':

        # CREAR: un formulario UsuarioForm con los datos del usuario actual
        # CREAR: un formulario RegistroPerfilForm con los datos del usuario actual
        pass
    
    # CREAR: variable de contexto para enviar formulario de usuario y perfil
    context = { }

    return render(request, 'core/misdatos.html', context)

@login_required
def boleta(request, nro_boleta):

    # CREAR: lógica para ver la boleta
    
    # CREAR: variable de contexto para enviar boleta y detalle de la boleta
    context = { }

    return render(request, 'core/boleta.html', context)

@user_passes_test(es_personal_autenticado_y_activo)
def ventas(request):
    
    # CREAR: lógica para ver las ventas

    # CREAR: variable de contexto para enviar historial de ventas
    context = { }

    return render(request, 'core/ventas.html', context)

@user_passes_test(es_personal_autenticado_y_activo)
def productos(request, accion, id):
    
    if request.method == 'POST':
        
        # CREAR: lógica para crear y actualizar un producto
        pass

    if request.method == 'GET':

        # CREAR: lógica para preparar la página para la acción de: crear, actualizar y eliminar un producto
        pass

    # CREAR: variable de contexto para enviar el formulario y todos los productos
    context = { }

    return render(request, 'core/productos.html', context)

@user_passes_test(es_personal_autenticado_y_activo)
def usuarios(request, accion, id):
    
    # CREAR: variables de usuario y perfil

    if request.method == 'POST':

        # CREAR: un formulario UsuarioForm para recuperar datos del formulario asociados al usuario
        # CREAR: un formulario PerfilForm para recuperar datos del formulario asociados al perfil del usuario
        # CREAR: lógica para actualizar los datos del usuario
        pass
    
    if request.method == 'GET':

        if accion == 'eliminar':
            # CREAR: acción de eliminar un usuario
            pass
        else:
            # CREAR: un formulario UsuarioForm asociado al usuario
            # CREAR: un formulario PerfilForm asociado al perfil del usuario
            pass

    # CREAR: variable de contexto para enviar el formulario de usuario, formulario de perfil y todos los usuarios
    context = { }

    return render(request, 'core/usuarios.html', context)

@user_passes_test(es_personal_autenticado_y_activo)
def bodega(request):

    if request.method == 'POST':

        # CREAR: acciones para agregar productos a la bodega
        pass

    registros = Bodega.objects.all()
    lista = []
    for registro in registros:
        vendido = DetalleBoleta.objects.filter(bodega=registro).exists()
        item = {
            'bodega_id': registro.id,
            'nombre_categoria': registro.producto.categoria.nombre,
            'nombre_producto': registro.producto.nombre,
            'estado': 'Vendido' if vendido else 'En bodega',
            'imagen': registro.producto.imagen,
        }
        lista.append(item)

    context = {
        'form': BodegaForm(),
        'productos': lista,
    }
    
    return render(request, 'core/bodega.html', context)

@user_passes_test(es_personal_autenticado_y_activo)
def obtener_productos(request):
    # La vista obtener_productos la usa la pagina "Administracion de bodega", para
    # filtrar el combobox de productos cuando el usuario selecciona una categoria
    
    # CREAR: Un JSON para devolver los productos que corresponden a la categoria

    data = []
    return

@user_passes_test(es_personal_autenticado_y_activo)
def eliminar_producto_en_bodega(request, bodega_id):
    # La vista eliminar_producto_en_bodega la usa la pagina "Administracion de bodega", 
    # para eliminar productos que el usuario decidio sacar del inventario

    # CREAR: lógica para eliminar un producto de la bodega

    return redirect(bodega)

@user_passes_test(es_cliente_autenticado_y_activo)
def miscompras(request):

    # CREAR: lógica para ver las compras del cliente

    # CREAR: variable de contexto para enviar el historial de compras del cliente
    context = { }

    return render(request, 'core/miscompras.html', context)


#COMPLETO***************************************************************************************************#

# VISTA PARA CAMBIAR ESTADO DE LA BOLETA

@user_passes_test(es_personal_autenticado_y_activo)
def cambiar_estado_boleta(request, nro_boleta, estado):
    boleta = Boleta.objects.get(nro_boleta=nro_boleta)
    if estado == 'Anulado':
        # Anular boleta, dejando la fecha de anulación como hoy y limpiando las otras fechas
        boleta.fecha_venta = date.today()
        boleta.fecha_despacho = None
        boleta.fecha_entrega = None
    elif estado == 'Vendido':
        # Devolver la boleta al estado recien vendida al dia de hoy, y sin despacho ni entrega
        boleta.fecha_venta = date.today()
        boleta.fecha_despacho = None
        boleta.fecha_entrega = None
    elif estado == 'Despachado':
        # Cambiar boleta a estado despachado, se conserva la fecha de venta y se limpia la fecha de entrega
        boleta.fecha_despacho = date.today()
        boleta.fecha_entrega = None
    elif estado == 'Entregado':
        # Cambiar boleta a estado entregado, pero hay que ver que estado actual tiene la boleta
        if boleta.estado == 'Vendido':
            # La boleta esta emitida, pero sin despacho ni entrega, entonces despachamos y entregamos hoy
            boleta.fecha_despacho = date.today()
            boleta.fecha_entrega = date.today()
        elif boleta.estado == 'Despachado':
            # La boleta esta despachada, entonces entregamos hoy
            boleta.fecha_entrega = date.today()
        elif boleta.estado == 'Entregado':
            # La boleta esta entregada, pero si se trata de un error entonces entregamos hoy
            boleta.fecha_entrega = date.today()
    boleta.estado = estado
    boleta.save()
    return redirect(ventas)


# FUNCIONES AUXILIARES PARA OBTENER: INFORMACION DE PRODUCTOS, CALCULOS DE PRECIOS Y OFERTAS

def obtener_info_producto(producto_id):

    producto = Producto.objects.get(id=producto_id)

    stock = Bodega.objects.filter(producto_id=producto_id).exclude(detalleboleta__isnull=False).count()
    
    con_oferta = f'<span class="text-primary"> EN OFERTA {producto.descuento_oferta}% DE DESCUENTO </span>'
    sin_oferta = '<span class="text-success"> DISPONIBLE EN BODEGA </span>'
    agotado = '<span class="text-danger"> AGOTADO </span>'

    if stock == 0:
        estado = agotado
    else:
        estado = sin_oferta if producto.descuento_oferta == 0 else con_oferta

    en_stock = f'En stock: {formatear_numero(stock)} {"unidad" if stock == 1 else "unidades"}'
   
    return {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'imagen': producto.imagen,
        'html_estado': estado,
        'html_precio': obtener_html_precios_producto(producto),
        'html_stock': en_stock,
    }

def obtener_html_precios_producto(producto):
    
    precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr = calcular_precios_producto(producto)
    
    normal = f'Precio: {formatear_dinero(precio_normal)}'
    tachar = f'Precio: <span class="text-decoration-line-through"> {formatear_dinero(precio_normal)} </span>'
    oferta = f'Oferta: <span class="text-success"> {formatear_dinero(precio_oferta)} </span>'
    subscr = f'Subscrito: <span class="text-danger"> {formatear_dinero(precio_subscr)} </span>'

    if hay_desc_oferta > 0:
        texto_precio = f'{tachar}<br>{oferta}'
    else:
        texto_precio = normal

    if hay_desc_subscr > 0:
        texto_precio += f'<br>{subscr}'

    return texto_precio

def calcular_precios_producto(producto):
    precio_normal = producto.precio
    precio_oferta = producto.precio * (100 - producto.descuento_oferta) / 100
    precio_subscr = producto.precio * (100 - (producto.descuento_oferta + producto.descuento_subscriptor)) / 100
    hay_desc_oferta = producto.descuento_oferta > 0
    hay_desc_subscr = producto.descuento_subscriptor > 0
    return precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr

# VISTAS y FUNCIONES DE COMPRAS

def comprar_ahora(request):
    messages.error(request, f'El pago aún no ha sido implementado.')
    return redirect(index)

@user_passes_test(es_cliente_autenticado_y_activo)
def carrito(request):

    detalle_carrito = Carrito.objects.filter(cliente=request.user.perfil)

    total_a_pagar = 0
    for item in detalle_carrito:
        total_a_pagar += item.precio_a_pagar
    monto_sin_iva = int(round(total_a_pagar / 1.19))
    iva = total_a_pagar - monto_sin_iva

    context = {
        'detalle_carrito': detalle_carrito,
        'monto_sin_iva': monto_sin_iva,
        'iva': iva,
        'total_a_pagar': total_a_pagar,
    }

    return render(request, 'core/carrito.html', context)

def agregar_producto_al_carrito(request, producto_id):

    if es_personal_autenticado_y_activo(request.user):
        messages.error(request, f'Para poder comprar debes tener cuenta de Cliente, pero tu cuenta es de {request.user.perfil.tipo_usuario}.')
        return redirect(index)
    elif es_usuario_anonimo(request.user):
        messages.info(request, 'Para poder comprar, primero debes registrarte como cliente.')
        return redirect(registro)

    perfil = request.user.perfil
    producto = Producto.objects.get(id=producto_id)

    precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr = calcular_precios_producto(producto)

    precio = producto.precio
    descuento_subscriptor = producto.descuento_subscriptor if perfil.subscrito else 0
    descuento_total=producto.descuento_subscriptor + producto.descuento_oferta if perfil.subscrito else producto.descuento_oferta
    precio_a_pagar = precio_subscr if perfil.subscrito else precio_oferta
    descuentos = precio - precio_subscr if perfil.subscrito else precio - precio_oferta

    Carrito.objects.create(
        cliente=perfil,
        producto=producto,
        precio=precio,
        descuento_subscriptor=descuento_subscriptor,
        descuento_oferta=producto.descuento_oferta,
        descuento_total=descuento_total,
        descuentos=descuentos,
        precio_a_pagar=precio_a_pagar
    )

    return redirect(ficha, producto_id)

@user_passes_test(es_cliente_autenticado_y_activo)
def eliminar_producto_en_carrito(request, carrito_id):
    Carrito.objects.get(id=carrito_id).delete()
    return redirect(carrito)

@user_passes_test(es_cliente_autenticado_y_activo)
def vaciar_carrito(request):
    productos_carrito = Carrito.objects.filter(cliente=request.user.perfil)
    if productos_carrito.exists():
        productos_carrito.delete()
        messages.info(request, 'Se ha cancelado la compra, el carrito se encuentra vacío.')
    return redirect(carrito)


# CAMBIO DE PASSWORD Y ENVIO DE PASSWORD PROVISORIA POR CORREO

@login_required
def mipassword(request):

    if request.method == 'POST':

        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido actualizada con éxito, ingresa de nuevo con tu nueva contraseña.')
            return redirect(ingresar)
        else:
            messages.error(request, 'Tu contraseña no pudo ser actualizada.')
            show_form_errors(request, [form])
    
    if request.method == 'GET':

        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form
    }

    return render(request, 'core/mipassword.html', context)

@user_passes_test(es_personal_autenticado_y_activo)
def cambiar_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        existe = User.objects.filter(username=username).exists()
        if existe:
            user = User.objects.get(username=username)
            if user is not None:
                if user.is_active:
                    password = User.objects.make_random_password()
                    user.set_password(password)
                    user.save()
                    enviado = enviar_correo_cambio_password(request, user, password)
                    if enviado:
                        messages.success(request, f'Una nueva contraseña fue enviada al usuario {user.first_name} {user.last_name}')
                    else:
                        messages.error(request, f'No fue posible enviar la contraseña al usuario {user.first_name} {user.last_name}, intente nuevamente más tarde')
                else:
                    messages.error(request, 'La cuenta está desactivada.')
            else:
                messages.error(request, 'La cuenta o la password no son correctos')
        else:
            messages.error(request, 'El usuario al que quiere generar una nueva contraseña ya no existe en el sistema')
    return redirect(usuarios, 'crear', '0')

def enviar_correo_cambio_password(request, user, password):
    try:
        # Revisar "CONFIGURACIÓN PARA ENVIAR CORREOS ELECTRÓNICOS A TRAVÉS DEL SERVIDOR DE GMAIL" en settings.py 
        subject = 'Cambio de contraseña Sword Games Shop'
        url_ingresar = request.build_absolute_uri(reverse(ingresar))
        message = render(request, 'common/formato_correo.html', {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_password': password,
            'link_to_login': url_ingresar,
        })
        from_email = 'info@faithfulpet.com'  # La dirección de correo que aparecerá como remitente
        recipient_list = []
        recipient_list.append(user.email)
        # Enviar el correo
        send_mail(subject=subject, message='', from_email=from_email, recipient_list=recipient_list
            , html_message=message.content.decode('utf-8'))
        return True
    except:
        return False


# POBLAR BASE DE DATOS CON REGISTROS DE PRUEBA

def poblar(request):
    # Permite poblar la base de datos con valores de prueba en todas sus tablas.
    # Opcionalmente se le puede enviar un correo único, para que los Administradores
    # del sistema puedan probar el cambio de password de los usuarios, en la página
    # de "Adminstración de usuarios".
    poblar_bd('caro.aguirre@duocuc.cl')
    return redirect(index)
