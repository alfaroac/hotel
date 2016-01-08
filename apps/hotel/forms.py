from django import forms
from .models import Habitacion, Registro

class HabitacionForm(forms.ModelForm):
	class Meta:
		model=Habitacion
 		exclude=()

 		
class RegistroForm(forms.ModelForm):
	class Meta:
		model=Registro
 		exclude=()
