from django import forms


from .models import Usuarios

class AmigoForm(forms.ModelForm): 
	class Meta:
		model = Usuarios
		fields = ["nombre", "apellido"]