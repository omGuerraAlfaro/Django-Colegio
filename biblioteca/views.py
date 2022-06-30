from django.shortcuts import render, redirect
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
