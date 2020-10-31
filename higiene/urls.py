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
    path ('productos_general',views.productos_general, name='productos_general'),
    path ('eliminar_productos',views.eliminar_productos, name='eliminar_productos'),
    path ('listar_productos',views.listar_productos, name='listar_productos'),

]