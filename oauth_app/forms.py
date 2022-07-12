from pyexpat import model
from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	error_messages = {
		'password_mismatch': ("Las Contraseñas no coinciden"),
	}
	username = forms.CharField(label='Nombre de usuario')
	first_name = forms.CharField(max_length=30, required=False, label='Nombre')
	last_name = forms.CharField(max_length=30, required=False, label='Apellido')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Correo Electronico', error_messages={'invalid':'El Correo ingresado es Invalido'})
	password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
	password2 = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña')
	is_staff = forms.BooleanField( required=False, label='Permisos Administracion')
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2','is_staff')
