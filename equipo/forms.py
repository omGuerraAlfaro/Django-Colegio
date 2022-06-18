from django import forms
from django.forms import ModelForm
from .models import Docente

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = ['rut','nombre','apellidoPat','apellidoMat', 'correo','imagen','asignatura']
    def __init__(self, *args, **kwargs):
        super(DocenteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class ModDocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre','apellidoPat','apellidoMat', 'correo','asignatura']
    def __init__(self, *args, **kwargs):
        super(ModDocenteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
