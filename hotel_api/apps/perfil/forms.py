# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TipoUsuarioForm(forms.ModelForm):

    class Meta:
        model = TipoUsuario
        exclude = ()
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de usuario'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class PerfilForm(forms.ModelForm):

    class Meta:
        # model=User
        model = Perfil
        exclude = ()
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono (opcional)'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese DNI'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese código'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese dirección'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese celular'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'btn btn-default form-control'}),
        }

SEX = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class UserRegisterForm(UserCreationForm):

    rol = forms.ModelChoiceField(
        queryset=TipoUsuario.objects.all(), widget = forms.Select(attrs={'class': 'form-control'}),)
    dni = forms.CharField(max_length=8, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese DNI'}), )
    sexo = forms.ChoiceField(choices=SEX, widget = forms.Select(attrs={'class': 'form-control'}),)
    telefono = forms.CharField(max_length=8, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese telefono'}), )
    codigo = forms.CharField(max_length=12, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese código'}),)
    direccion = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese direción'}),)
    celular = forms.CharField(max_length=13, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese celular'}),)
    estado = forms.BooleanField(required=True)
    imagen = forms.ImageField(widget = forms.ClearableFileInput(attrs={'class': 'file'}),)

    class Meta:

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1' )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese password'}),
        }

class UserForm(UserCreationForm):

    codigo = forms.CharField(max_length=12, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese código'}),)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','is_staff',)
        exclude = ('is_staff', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ingrese Usuario'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Ingresa un email'}),
            'password1': forms.TextInput(attrs={
                'type': 'password', 'class': 'form-control',
                # 'disabled':'True',
                'placeholder': 'Ingrese password'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ingrese Nombres'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ingrese Apellidos'}),
        }
