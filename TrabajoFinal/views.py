from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

#from .forms import CustomUserForm


def Inicio(request):
	return render(request,'Pag_ppal.html')

def Nosotros(request):
	return render(request, 'Nosotros.html')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('login')
	else:
		form = UserRegisterForm()
	context = { 'form' : form }
	return render(request, 'usuarios/register.html', context)


