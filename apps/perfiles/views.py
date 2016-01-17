from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.views.generic import TemplateView
#from django.contrib.auth.decorators import login_required
from .forms import HuespedForm, RolesForm
from .models import Huesped, Personal, Rol
from apps.hotel.models import Habitacion
from django.http import HttpResponse
import json

#@login_required
def main(request):
	lista=Habitacion.objects.all()
	return render(request, 'index.html', {'lista':lista})


def huesped(request):
	lista = Huesped.objects.all()
	numreg=lista.count()
	return render(request,'huesped/huesped.html', {'lista':lista, 'cantidad':numreg})

def addHuesped(request):
	if request.method=='POST':
		objform=HuespedForm(request.POST)
		if objform.is_valid():
			objform.save()
			return render(request,'huesped/addHuesped.html', {'form':objform})
	else:
		objform=HuespedForm()
	return render(request,'huesped/addHuesped.html', {'form':objform})

def updHuesped(request, id):
	objedit=Huesped.objects.get(pk=id)
	if request.method=='POST':
		objform=HuespedForm(request.POST,instance=objedit)
		if objform.is_valid():
			objform.save()
			return render(request, 'huesped/updHuesped.html', {'form':objform}, context_instance=RequestContext(request))
	else:
		objform=HuespedForm(instance=objedit)
	return render(request, 'huesped/updHuesped.html', {'form':objform}, context_instance=RequestContext(request))

def delHuesped(request, id, template_name = 'huesped/delHuesped.html'):
	obj_delete=Huesped.objects.get(pk=id)
	if request.method=='POST':
		obj_delete.delete()
		return redirect(reverse('perfiles_app:huesped'))
	return render(request, template_name, {'object':obj_delete})


class buscarPorDni(TemplateView):
	def post(self, request, *args, **kwargs):
		buscar=request.POST['buscalo']
		huesped=Huesped.objects.filter(dni__contains=buscar)
		return render(request,'huesped/buscarHuesped.html', {'huespedes':huesped})

def listPersonal(request):
	lista=Personal.objects.all()
	cantidad = lista.count()
	return render(request, 'personal/personal.html', {'lista':lista, 'cantidad':cantidad})

def listRoles(request):
	lista=Rol.objects.all()
	cantidad = lista.count()
	return render(request, 'rol/roles.html', {'lista':lista, 'cantidad':cantidad})

def addRoles(request):
	if request.method=='POST':
		objform=RolesForm(request.POST)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:roles'))
	else:
		objform=RolesForm()
	return render(request,'rol/addRoles.html', {'form':objform})

def updRoles(request, id):
	objedit=Rol.objects.get(pk=id)
	if request.method=='POST':
		objform=RolesForm(request.POST,instance=objedit)
		if objform.is_valid():
			objform.save()
			return render(request, 'rol/updRoles.html', {'form':objform}, context_instance=RequestContext(request))
	else:
		objform=RolesForm(instance=objedit)
	return render(request, 'rol/updRoles.html', {'form':objform}, context_instance=RequestContext(request))
