from django.shortcuts 				import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins 	import LoginRequiredMixin
from django.views.generic 			import ListView, CreateView
from .models 						import Usuarios
from .forms 						import AmigoForm
from django.urls 					import reverse_lazy
from django.views.generic.edit		import UpdateView
# Create your views here.
"""
def listar_usuarios(request): 
	template_name = "usuarios/listarusuarios.html"
	lista_de_usuarios = Usuarios.objects.all()
	ctx = {
		'usuarios' : lista_de_usuarios
	}
	return render(request, template_name, ctx)
"""


"""
def nuevo_amigo(request): 
	template_name = "usuarios/nuevo.html"

	if request.method == "POST":
		nombre = request.POST.get("nombre", None)
		apellido = request.POST.get("apellido", None)
		a = Usuarios.objects.create(nombre=nombre, apellido=apellido)

		return redirect('usuarios:listar')

	ctx = {
		'form': AmigoForm()
	}
	return render(request, template_name, ctx)




def editar_amigo(request, pk): 
	template_name = "usuarios/editar.html"
	ctx = {
		'usuarios': Usuarios.objects.get(id=pk)
	}
	return render(request, template_name, ctx)
"""

class EditarAmigo(UpdateView):
	template_name = "usuarios/editar.html"
	model = Usuarios
	form_class = AmigoForm

	def get_success_url(self, **kwargs): 
		return reverse_lazy("usuarios:listar")


class CrearAmigo(CreateView):
	template_name = "usuarios/nuevo.html"
	model = Usuarios
	form_class = AmigoForm

	def get_success_url(self, **kwargs): 
		return reverse_lazy("usuarios:listar")


class Listar(LoginRequiredMixin, ListView): 
	template_name = "usuarios/listarusuarios.html" # Seguir despues, tiene un error... video Vistas basadas en funciones
													
	model = Usuarios
	
	context_object_name = 'usuarios'

	def get_queryset(self): 
		if self.request.user.is_superuser: 
			return Usuarios.objects.all()
		

		return Usuarios.objects.filter(nombre="Belen")

	"""
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["color"] = "amarillo"
		return context
	"""