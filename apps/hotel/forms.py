from django import forms
from .models import Habitacion, Registro
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets


class HabitacionForm(forms.ModelForm):

    class Meta:
        model = Habitacion
        exclude = ()
        widgets = {
        'numero':forms.TextInput(attrs={'class':'form-control col-sm-4'}),
        'piso':forms.TextInput(attrs={'class':'form-control col-sm-4'}),
        'tipo':forms.Select(attrs={'class':'form-control col-sm-4'}),
        'descripcion':forms.Textarea(attrs={'class':'form-control col-sm-4', 'cols':'30', 'rows':'3'}),
        'estado':forms.Select(attrs={'class':'form-control col-sm-4'}),        
        }


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        exclude = ()
       	widgets={
        #'fec_ingreso':forms.SelectDateWidget(),DateField(initial=datetime.date.today)
        'fec_ingreso':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        'huesped':forms.Select(attrs={'class':'form-control'}),
        'habitacion':forms.Select(attrs={'class':'form-control'}),
        'fec_salida':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        'tarifa':forms.NumberInput(attrs={'class':'form-control'}),
        'forma_pago':forms.Select(attrs={'class':'form-control'}),
        }


# class RegistroFormp(forms.ModelForm):

#     class Meta:
# 	    nombre = forms.CharField(max_length=15)