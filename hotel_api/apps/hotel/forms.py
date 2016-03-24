from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Sucursal


class SucursalForm(forms.ModelForm):

    class Meta:
        model = Sucursal
        # fields = ('',)
        exclude = ()


# class UsersForm(UserCreationForm):
# 	class Meta:
# 		model=User
#  		exclude=()
#  		widgets={
#  		'username':forms.TextInput(attrs={'class':'form-control'}),
#  		'user':forms.TextInput(attrs={'class':'form-control'}),
#  		'first_name':forms.TextInput(attrs={'class':'form-control'}),
#  		'last_name':forms.TextInput(attrs={'class':'form-control'}),
#  		'email':forms.EmailInput(attrs={'class':'form-control'}),
#  		'password':forms.TextInput(attrs={'class':'form-control'}),
#  		}
