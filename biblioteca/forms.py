from django import forms
from django.forms import ModelForm
from rest_taller.models import Libro

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['sku','autor','nombreLibro','genero','dias']
    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            