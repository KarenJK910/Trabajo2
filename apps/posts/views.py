from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Ods, Posts
from .forms import Formulario_alta_post

# si la vista es basada en funcion
from django.contrib.auth.decorators import login_required

#si la vista es basada en clase
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
@login_required
def Posts_Destacados(request):
	p = Posts.objects.all()
	ctx= {}
	ctx['posts'] = p
	ctx['titulo'] = 'Hola soy el titulo'
	

	return render (request,'Pag_ppal.html',ctx)


class AltaPost(LoginRequiredMixin,CreateView):
	model= 'Posts'
	template_name = 'Posts/alta.html'
	form_class = Formulario_alta_post
	success_url= reverse_lazy('primera_vista')


def filtro(request, pk):
	p = Posts.objects.filter(Ods = pk)
	
	ctx = {}
	ctx['posts'] = p
	
	return render (request,'Posts/Filtro.html',ctx)	


def DetallePost(request, pk):

	p = Posts.objects.get(pk = pk)
	ctx = {}
	ctx['posts'] = p
	

	return render(request, 'Posts/detallePost.html', ctx)
	












'''
# Create your views here.
def Listar_Productos(request):

	#consulta para traer los productos.
	p = Producto.objects.all()  #select * from productos
	#para mandarlo al template se usa un contexto

	ctx= {}
	ctx['product'] = p
	ctx['titulo'] = 'Hola soy el titulo'

	return render (request,'producto/listar_producto.html',ctx)


def DetalleProducto(request,pk):
	return render(request,productos/DetalleProducto.html)

def DetalleProducto(request,pk):


# Create your views here.
'''
