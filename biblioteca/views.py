from django.shortcuts import render, redirect
<<<<<<< HEAD
from biblioteca.Carrito import Carrito
=======
from biblioteca import Carrito
>>>>>>> db02c729f71cbe21c845ed1ccb3028b66abf341f
from biblioteca.models import Producto
from rest_taller.models import Libro
from rest_taller.serializers import LibroSerializer
from .forms import LibroForm

# Create your views here.
def listar_libros(request):
    books = Libro.objects.all()
    datos = {'listar_libros':books}
    return render(request,'biblioteca/biblioteca.html',datos)

def agregarLibro(request):
    
    datos= {
        'formLibro':LibroForm()
    }

    if (request.method == 'POST'):
        #rescatar la informacion
        formulario = LibroForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save() 
            datos['mensaje'] = 'Libro agregado'
        else:
            #mensaje de error
            datos['mensaje'] = 'No se agrego el libro'
    
    return render(request,'biblioteca/agregar_libro.html',datos)

def modificarLibro(request,id):
    book = Libro.objects.get(sku=id)

    datos={
        'formLibro':LibroForm(instance=book)
    }

    if (request.method == 'POST'):
        formUpdate = LibroForm(request.POST, request.FILES,instance=book)
        if formUpdate.is_valid():
            formUpdate.save() 
            datos['mensaje'] = 'Libro Modificado'
            return redirect(to='listar_libros')
        else:
            #mensaje de error
            datos['mensaje'] = 'No se pudo modificar el libro'

    return render(request,'biblioteca/modificar_libro.html',datos)

def eliminarLibro(request,id):
    book =  Libro.objects.get(sku=id)
    book.delete()
    return redirect(to='listar_libros')



""" Funciones Carrito """
def tienda (request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
<<<<<<< HEAD
    Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    Carrito(request).agregar(producto)
=======
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
>>>>>>> db02c729f71cbe21c845ed1ccb3028b66abf341f
    return redirect("Tienda")

def eliminar_producto(request, produto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=produto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, produto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=produto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")