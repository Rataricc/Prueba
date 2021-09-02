from django.db                  import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
	apodo = models.CharField(max_length=22, null=True, blank=True)
	fecha_de_nacimiento = models.DateField(null=True,blank=True)
	direccion = models.CharField(max_length=255, null=True, blank=True)

	class Meta: 
		db_table = 'user' 