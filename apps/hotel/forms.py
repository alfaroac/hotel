from django import forms
from .models import Habitacion, Registro
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets 

class HabitacionForm(forms.ModelForm):
	class Meta:
		model=Habitacion
 		exclude=()

 		
class RegistroForm(forms.ModelForm):
	class Meta:
		model=Registro
		fields = ['fec_ingreso', 'huesped', 'habitacion','fec_salida','tarifa','forma_pago']
 		exclude=()

	def __init__(self, *args, **kwargs):
		super(RegistroForm, self).__init__(*args, **kwargs)
		self.fields['fec_ingreso'].widget = widgets.AdminSplitDateTime()
		self.fields['fec_salida'].widget = widgets.AdminSplitDateTime()