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
  #      	widgets={
		#'fec_ingreso':forms.TextInput(attrs={'class':'form-control col-md-6'}),
		# 'nameInstitution':forms.TextInput(attrs={'class':'form-control'}),
		# 'address':forms.TextInput(attrs={'class':'form-control'}),
		# 'latitude':forms.TextInput(attrs={'class':'form-control'}),
		# 'longitude':forms.TextInput(attrs={'class':'form-control'}),
		# 'state':forms.CheckboxInput(attrs={'class':'form-control'}),
		# }



    #def __init__(self, *args, **kwargs):
    #   super(RegistroForm, self).__init__(*args, **kwargs)
    #   self.fields['fec_ingreso'].widget = widgets.AdminSplitDateTime()
    #   self.fields['fec_salida'].widget = widgets.AdminSplitDateTime()

# class DatePicker(forms.DateInput):
#     template_name = 'hotel/registro/addRegistro.html'

#     class Media:
#         js = (
#             'js/jquery.min.js',
#             'js/jquery-ui.min.js',
#         )
#         css = {
#             'all': (
#                 'css/jquery-ui.css',
#             )
#         }


# class DateForm(forms.Form):
#     date = forms.DateField(widget=DatePicker)