from django import forms
from .models import Posts

class Formulario_alta_post(forms.ModelForm):
	

	class Meta:
		model = Posts
		fields= '__all__'
		