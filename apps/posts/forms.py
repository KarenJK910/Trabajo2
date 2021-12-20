from django import forms
from django.db.models.fields import CommaSeparatedIntegerField
from django.forms import widgets
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
		fields= ( "name", "body","Posts")
		widgets = {
			"name": forms.TextInput(attrs={"class": "col-sm-12"}),
		    "body": forms.Textarea(attrs={"class": "col-sm-12"}),

		}







		

