from django.shortcuts import render
from .models import Ods, Posts

# Create your views here.
def Posts_Destacados(request):
	p = Posts.objects.all()
	ctx= {}
	ctx['posts'] = p
	ctx['titulo'] = 'Hola soy el titulo'

	return render (request,'Pag_ppal.html',ctx)




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
