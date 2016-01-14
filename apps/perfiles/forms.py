from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Huesped

class HuespedForm(forms.ModelForm):
    class Meta:
        model=Huesped
        exclude=()
        widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control'}),
        'apellidos':forms.TextInput(attrs={'class':'form-control'}),
        'dni':forms.NumberInput(attrs={'class':'form-control'}),
        'fecha_nac':forms.SelectDateWidget(attrs={'class':'form'}),
        'sexo':forms.Select(attrs={'class':'form-control'}),
        'telefono':forms.NumberInput(attrs={'class':'form-control'}),
        'nacionalidad':forms.TextInput(attrs={'class':'form-control'}),
        'procedencia':forms.TextInput(attrs={'class':'form-control'}),
        }