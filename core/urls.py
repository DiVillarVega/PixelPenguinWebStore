from django.urls import path
from .views import index, ficha, registro, nosotros, productos, usuarios, bodega
from .views import ventas, boleta, ingresar, misdatos, miscompras, carrito, ropa, poblar

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('registro', registro, name='registro'),
    path('nosotros', nosotros, name='nosotros'),
    path('productos/<accion>/<id>', productos, name='productos'),
    path('usuarios/<accion>/<id>', usuarios, name='usuarios'),
    path('bodega', bodega, name='bodega'),
    path('ventas', ventas, name='ventas'),
    path('boleta/<nro_boleta>', boleta, name='boleta'),
    path('ingresar', ingresar, name='ingresar'),
    path('misdatos', misdatos, name='misdatos'),
    path('miscompras', miscompras, name='miscompras'),
    path('carrito', carrito, name='carrito'),
    path('ropa', ropa, name='ropa'),
    path('poblar', poblar, name='poblar')
    
    #path('salir', salir, name='salir'),
    #path('cambiar_password', cambiar_password, name='cambiar_password'),
    #path('obtener_productos', obtener_productos, name='obtener_productos'),
    #path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    #path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    #path('mipassword', mipassword, name='mipassword'),
    #path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    #path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    #path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
]