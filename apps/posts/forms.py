from django import forms
from django.db.models.fields import CommaSeparatedIntegerField
from .models import Posts
from django import forms
from .models import Comentarios
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario


class Formulario_alta_post(forms.ModelForm):
	

	class Meta:
		model = Posts
		fields= '__all__'


class NuevoComentario(forms.ModelForm):
	

	class Meta:
		model = Comentarios
		fields= '__all__'






		

