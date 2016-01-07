from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
from .forms import HuespedForm
from .models import Huesped
from django.http import HttpResponse
import json

#@login_required
def main(request):
	return render(request, 'index.html')

# def busqueda(request):
#     if request.is_ajax(): 
#     	objbuscado = Huesped.objects.filter(nombre__startswith= request.GET['nombre']).values('nombre', 'id','dni')
#         return HttpResponse( json.dumps( list(objbuscado)), content_type='application/json') 
#     else: 
#         return HttpResponse("Solo Ajax")


def huesped(request):
	lista = Huesped.objects.all()
	numreg=lista.count()
	return render(request,'huesped/huesped.html', {'lista':lista, 'cantidad':numreg})

def addHuesped(request):
	if request.method=='POST':
		objform=HuespedForm(request.POST)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:huesped'))
	else:
		objform=HuespedForm()
	return render(request,'huesped/addHuesped.html', {'form':objform})

def updHuesped(request, id):
	objedit=Huesped.objects.get(pk=id)
	if request.method=='POST':
		objform=HuespedForm(request.POST,instance=objedit)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:huesped'))
	else:
		objform=HuespedForm(instance=objedit)
	return render(request, 'huesped/updHuesped.html', {'form':objform}, context_instance=RequestContext(request))

def delHuesped(request, id, template_name = 'huesped/delHuesped.html'):
	obj_delete=Huesped.objects.get(pk=id)
	if request.method=='POST':
		obj_delete.delete()
		return redirect(reverse('perfiles_app:huesped'))
	return render(request, template_name, {'object':obj_delete})
