from django.db import models

# Create your models here.


class Usuarios(models.Model): 
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)

	class Meta: 
		db_table = 'usuarios'

	def __str__(self): 
		return self.nombre
