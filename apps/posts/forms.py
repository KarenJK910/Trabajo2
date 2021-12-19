from django import forms
from django.db.models.fields import CommaSeparatedIntegerField
from .models import Posts
from django import forms
from .models import Comentarios


class Formulario_alta_post(forms.ModelForm):
	

	class Meta:
		model = Posts
		fields= '__all__'


class NuevoComentario(forms.ModelForm):
	

	class Meta:
		model = Comentarios
		fields= '__all__'




		

