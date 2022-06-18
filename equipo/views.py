from django.shortcuts import render,redirect
from .models import Docente
from .forms import DocenteForm,ModDocenteForm
from django.contrib import messages
MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'critical',
}
# Create your views here.
def equipo(request):
    listaDocentes= Docente.objects.all()
    datos = {
        'docentes': listaDocentes
    }
    return render(request, 'equipo/equipo.html',datos)

def agregarDocente(request):
    datos = {
        'form' :  DocenteForm() #se construye el modelo base. en base a form.py
    }

    if (request.method == 'POST'): #lo que haria el boton metodo post.
        formulario = DocenteForm(request.POST) #formulario: id de formulario del html
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Profesor agregado'
        else:
            datos['mensaje'] = 'Profesor No fue agregado'
    return render(request,'equipo/agregar_docente.html', datos)

def modificarDocente(request, id):
    seleccionado = Docente.objects.get(rut=id) #select * from vehiculo where patente = id

    datos = {
        'form': ModDocenteForm(instance=seleccionado)
    }

    if (request.method == 'POST'):
        formulario = ModDocenteForm(data=request.POST, instance=seleccionado)
        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Docente  se modificó'

            messages.success(request, 'Docente modificado')
            return redirect(to='equipo')
        else:
            datos['mensaje'] = 'Docente NO se modificó'

    return render(request,'equipo/modificar_docente.html', datos)    

def eliminarDocente(request, id):
    seleccionado = Docente.objects.get(rut=id)
    seleccionado.delete() # delete from Vehiculo where patente = id

    return redirect(to='equipo')
