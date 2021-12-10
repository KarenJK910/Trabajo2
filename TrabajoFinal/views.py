from django.shortcuts import render 

def Inicio(request):
	return render(request,'Pag_ppal.html')

def Nosotros(request):
	return render(request, 'Nosotros.html')