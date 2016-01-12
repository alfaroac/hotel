from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required

from .forms import HabitacionForm, RegistroForm
from .models import Habitacion, Registro

#import json

def habitacion(request):
    lista = Habitacion.objects.all()
    numreg=lista.count()
    return render(request,'hotel/habitacion/habitacion.html', {'lista':lista, 'cantidad':numreg})

def addHabitacion(request):
    if request.method=='POST':
        objform=HabitacionForm(request.POST)
        if objform.is_valid():
            objform.save()
            return redirect(reverse('hotel_app:habitacion'))
    else:
        objform=HabitacionForm()
    return render(request,'hotel/habitacion/addHabitacion.html', {'form':objform})

def updHabitacion(request, id):
    objedit=Habitacion.objects.get(pk=id)
    if request.method=='POST':
        objform=HabitacionForm(request.POST,instance=objedit)
        if objform.is_valid():
            objform.save()
            return redirect(reverse('hotel_app:habitacion'))
    else:
        objform=HabitacionForm(instance=objedit)
    return render(request, 'hotel/habitacion/updHabitacion.html', {'form':objform}, context_instance=RequestContext(request))

def delHabitacion(request, id, template_name = 'hotel/habitacion/delHabitacion.html'):
    obj_delete=Habitacion.objects.get(pk=id)
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('hotel_app:habitacion'))
    return render(request, template_name, {'object':obj_delete})

#registro
def registro(request):
    lista=Registro.objects.all()
    numreg=lista.count()
    return render(request,'hotel/registro/registro.html', {'lista':lista, 'cantidad':numreg})

def addRegistro(request):
    if request.method=='POST':
        objform=RegistroForm(request.POST)
        if objform.is_valid():
            objform.save()
            return redirect(reverse('hotel_app:registro'))
    else:
        objform=RegistroForm()
    return render(request,'hotel/registro/addRegistro.html', {'form':objform})

def updRegistro(request, id):
    objedit=Registro.objects.get(pk=id)
    if request.method=='POST':
        objform=RegistroForm(request.POST,instance=objedit)
        if objform.is_valid():
            objform.save()
            return redirect(reverse('hotel_app:registro'))
    else:
        objform=RegistroForm(instance=objedit)
    return render(request, 'hotel/registro/updRegistro.html', {'form':objform}, context_instance=RequestContext(request))

def delRegistro(request, id):
    objdel=Registro.objects.get(pk=id)
    if request.method=='POST':
        objdel.delete()
        return redirect(reverse('hotel_app:registro'))
    return render(request, 'hotel/registro/delRegistro.html', {'object':objdel})
