from django.shortcuts import render, redirect
from biblioteca.Carrito import Carrito
from biblioteca.models import Producto
from biblioteca.models import Prestamo
from rest_taller.models import Libro
import random
from rest_taller.serializers import LibroSerializer
from .forms import LibroForm
from datetime import datetime, timedelta

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
    Carrito(request)
    producto = Libro.objects.get(sku=producto_id)
    Carrito(request).agregar(producto)
    return redirect("listar_libros")

def eliminar_producto(request, produto_id):
    carrito = Carrito(request)
    producto = Libro.objects.get(sku=producto_id)
    carrito.eliminar(producto)
    return redirect("listar_libros")

def restar_producto(request, produto_id):
    carrito = Carrito(request)
    producto = Libro.objects.get(sku=producto_id)
    carrito.restar(producto)
    return redirect("listar_libros")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("listar_libros")

def solicitar_Libros(request):
    carrito = Carrito(request)
    libros = ''
    diasMax = 0
    fechadevolucion= datetime.today()
    numAleatorio = random.randint(1,10000) 
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            libros = libros + value["nombre"] + '- '
            if diasMax>value["dias"]:
               diasMax = diasMax
            elif diasMax<=value["dias"]:
                 diasMax = value["dias"]
            email = request.user.email
        if diasMax!=0:
            fechadevolucion= fechadevolucion + timedelta(days=diasMax)
            while Prestamo.objects.filter(cod_prestamo=numAleatorio).exists():
                Prestamo.objects.create(cod_prestamo=numAleatorio + 1, lista_libros=libros ,email=email ,fechaDevolucion=fechadevolucion, estado=0)
            else:
                Prestamo.objects.create(cod_prestamo=numAleatorio,lista_libros=libros ,email=email ,fechaDevolucion=fechadevolucion, estado=0)
        else: 
            carrito.limpiar()
    carrito.limpiar()
    return redirect('listar_libros')




def historial(request):
    if request.user.is_authenticated and request.user.is_staff:
        listarPrestamo = Prestamo.objects.all().order_by('-fechaDevolucion').values()
        datos = {'prestamo':listarPrestamo}

        return render(request,'biblioteca/Historial.html',datos)
    else:
        listarPrestamo = Prestamo.objects.filter(email=request.user.email).order_by('-fechaDevolucion').values()
        datos = {'prestamo':listarPrestamo}

        return render(request,'biblioteca/Historial.html',datos)
    
def devolucion(self,cod_prestamo):
    pres = Prestamo.objects.get(cod_prestamo=cod_prestamo)
    pres.estado = 1
    pres.save()

    return redirect('historial')