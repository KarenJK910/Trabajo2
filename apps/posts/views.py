from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Ods, Posts
from .forms import Formulario_alta_post


# Create your views here.
def Posts_Destacados(request):
	p = Posts.objects.all()
	ctx= {}
	ctx['posts'] = p
	ctx['titulo'] = 'Hola soy el titulo'

	return render (request,'Pag_ppal.html',ctx)


class AltaPost(CreateView):
	model= 'Posts'
	template_name = 'Posts/alta.html'
	form_class = Formulario_alta_post
	success_url= reverse_lazy('posts: Posts_Destacados')







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
