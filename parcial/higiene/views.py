from django.shortcuts import render
from .models import Producto
# Create your views here.

def menu_principal(request):
    print("ok, estamos en la vista menu principal")
    context={}
    return render(request,'higiene/menu_principal.html',context)

def comentarios(request):
    print("ok, estamos en la vista comentarios")
    context={}
    return render(request,'higiene/comentarios.html',context)

def quienesSomos(request):
    print("ok, estamos en la vista quienes Somos")
    context={}
    return render(request,'higiene/quienesSomos.html',context)

def buscar_productos(request):
    print("ok, estamos en la vista buscar productos")
    context={}
    return render(request,'higiene/buscar_productos.html',context)

def registro(request):
    print("ok, estamos en la vista registro")
    context={}
    return render(request, 'higiene/registro.html',context)

def agregarProducto(request):
    print("ok, estamos en la vista agregarProducto")
    context={}
    return render(request,'higiene/formulario_agregar.html',context)
    
def buscar(request):
    print("hola  estoy en buscar")
    if request.method == 'POST':
       mi_id = request.POST['buscarid']

       if mi_id != "":
        try:
            producto=Producto()
            producto= Producto.objects.get(id_producto=mi_id)
            if producto is not None:
                print("Producto=", producto)
                context={'producto':producto}
                return render(request,'higiene/buscar.html', context)
            else:
                return render(request, 'higiene/error/error_203.html', {})
        except producto.DoesNotExist:
            return render(request, 'higiene/error/error_204.html', {})
        else:
           return render(request, 'higiene/error/error_201.html', {})


def agregar(request):
    print("hola  estoy en agregar...")
    if request.method == 'POST':

       mi_nombre    = request.POST['nombre']
       mi_precio    = request.POST['precio']
       mi_fecha_env  = request.POST['calendar']
       mi_marca     = request.POST['marca']
       mi_imagen    = request.FILES['img']

       if mi_nombre != "":
           try:
               producto = Producto()

               producto.nombre = mi_nombre
               producto.apellido_paterno = mi_precio
               producto.fecha_env = mi_fecha_env
               producto.marca = mi_marca
               producto.imagen = mi_imagen

               producto.save()

               return render(request, 'higiene/mensaje_datos_grabados.html',{})

           except producto.DoesNotExist:
               return render(request, 'higiene/error/error_204.html', {})
       else:
           return render(request, 'higiene/error/error_201.html', {})
    else:
        return render(request, 'higiene/error/error_203.html', {})

def productos_general(request):
    print("ok, estamos en la vista productos_general")
    context={}
    return render(request,'higiene/productos_general.html',context)

def eliminar_por_id(request):
    print("hola  estoy en eliminar_por_id...")
    if request.method == 'POST':
       mi_id = request.POST['id']

       if mi_id != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(id_producto=mi_id)
               if producto is not None:
                   context ={}
                   producto.delete()
                   return render(request, 'higiene/mensaje_producto_eliminado.html',context)
               else:
                   return render(request, 'higiene/error/error_202.html',{})
           except producto.DoesNotExist:
               return render(request, 'higiene/error/error_202.html', {})
       else:
           return render(request, 'higiene/error/error_201.html', {})
    else:
        return render(request, 'higiene/error/error_203.html', {})

def eliminar_productos(request):
    print("ok, estamos en la vista eliminar_productos")
    context={}
    return render(request,'higiene/eliminar_productos.html',context)

def listar(request):
    print("ok, estamos en el listar")
    context ={}
    return render(request, 'higiene/listar.html', context)

def listar_productos(request):
    print("ok, estamos en la vista listar productos")
    lista = Producto.objects.all()
    context ={'listado':lista}
    return render(request, 'higiene/listar_productos.html', context)

def mensaje_datos_grabados(request):
    print("ok, estamos en la vista mensaje_datos_grabados")
    context={}
    return render(request,'higiene/mensaje_datos_grabados.html',context)

def mensaje_producto_eliminado(request):
    print("ok, estamos en la vista mensaje_producto_eliminado")
    context={}
    return render(request,'higiene/mensaje_producto_eliminado.html',context)

def modificar_productos(request):
    print("ok, estamos en la vista modificar_productos")
    context={}
    return render(request,'higiene/modificar_productos.html',context)

def buscar_modificar(request):
    print("hola  estoy en buscar_modificar")
    if request.method == 'POST':
       mi_id = request.POST['buscar_modificar']

       if mi_id != "":
        try:
            producto=Producto()
            producto= Producto.objects.get(id_producto=mi_id)
            if producto is not None:
                context={'producto':producto}
                return render(request,'higiene/formulario_modificar.html', context)
            else:
                return render(request, 'higiene/error/error_203.html', {})
        except producto.DoesNotExist:
            return render(request, 'higiene/error/error_204.html', {})
        else:
           return render(request, 'higiene/error/error_201.html', {})

def modificar(request):
    print("hola  estoy en modificar")
    if request.method == 'POST':

       mi_id        = request.POST['id_producto']
       mi_nombre    = request.POST['nombre']
       mi_precio    = request.POST['precio']
       mi_fecha_env  = request.POST['calendar']
       mi_marca     = request.POST['marca']
       mi_imagen    = request.FILES['img']

       if mi_nombre != "":
           try:
               producto = Producto()

               producto.id_producto = mi_id
               producto.nombre = mi_nombre
               producto.apellido_paterno = mi_precio
               producto.fecha_env = mi_fecha_env
               producto.marca = mi_marca
               producto.imagen = mi_imagen

               producto.save()

               return render(request, 'higiene/mensaje_datos_grabados.html',{})

           except producto.DoesNotExist:
               return render(request, 'higiene/error/error_204.html', {})
       else:
           return render(request, 'higiene/error/error_201.html', {})
    else:
        return render(request, 'higiene/error/error_203.html', {})