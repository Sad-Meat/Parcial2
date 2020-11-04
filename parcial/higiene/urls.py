from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .import views

urlpatterns = [
    path('menu_principal', views.menu_principal, name='menu_principal'),
    path('comentarios', views.comentarios, name='comentarios'),
    path('quienesSomos', views.quienesSomos, name='quienesSomos'),
    path('registro', views.registro, name='registro'),
    path ('agregarProducto',views.agregarProducto, name='agregarProducto'),
    path ('agregar',views.agregar, name='agregar'),
    path ('productos_general',views.productos_general, name='productos_general'),
    path ('eliminar_productos',views.eliminar_productos, name='eliminar_productos'),
    path ('eliminar_por_id',views.eliminar_por_id, name='eliminar_por_id'),
    path ('listar_productos',views.listar_productos, name='listar_productos'),
    path ('buscar_productos',views.buscar_productos, name='buscar_productos'),
    path ('buscar',views.buscar, name='buscar'),
    path ('mensaje_datos_grabados',views.mensaje_datos_grabados, name='mensaje_datos_grabados'),
    path ('mensaje_producto_eliminado',views.mensaje_producto_eliminado, name='mensaje_producto_eliminado'),
    path ('modificar_productos',views.modificar_productos, name='modificar_productos'),
    path ('buscar_modificar',views.buscar_modificar, name='buscar_modificar'),
    path ('modificar',views.modificar, name='modificar'),
]