from django.urls import path 
from . 			 import views  
# Esta url no viene por defecto con django cuando creamos una nueva app, entonces la tuve que crear yo.

app_name = "usuarios"

urlpatterns = [
	# path('listaru/', views.listar_usuarios, name= "listar"),
	path('listaru/', views.Listar.as_view(), name="listar"),
	# path('Nuevo/', views.nuevo_amigo, name="nuevo"),
	path('Nuevo/', views.CrearAmigo.as_view(), name="nuevo"),
	# path('Editar/<int:pk>/', views.editar_amigo, name="editar"),
	path('Editar/<int:pk>/', views.EditarAmigo.as_view(), name="editar")
]