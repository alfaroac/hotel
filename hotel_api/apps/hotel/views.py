# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
# from django.template import RequestContext
# from .models import Habitacion, Sucursal
# from .forms import SucursalForm


# @login_required
# def index(request):
#     lista = Habitacion.objects.all()
#     return render(request, 'hotel/main.html', {'lista': lista})


# @login_required
# def list_sucursal(request):
#     lista = Sucursal.objects.all()
#     if request.method == 'POST':
#         objform = SucursalForm(request.POST)
#         if objform.is_valid():
#             objform.save()
#             return redirect(reverse('sucursal'))
#     else:
#         objform = SucursalForm()
#     return render(request, 'sucursal/sucursal.html',
#                   {'listas': lista, 'form': objform})


# @login_required
# def upd_sucursal(request, id):
#     obj_edit = Sucursal.objects.get(pk=id)
#     if request.method == 'POST':
#         objform = SucursalForm(request.POST, instance=obj_edit)
#         if objform.is_valid():
#             objform.save()
#             return redirect(reverse('sucursal'))
#     else:
#         objform = SucursalForm(instance=obj_edit)
#     return render(request, 'sucursal/updSucursal.html',
#                   {'form': objform}, context_instance=RequestContext(request))


# @login_required
# def del_sucursal(request, id, template_name='sucursal/delSucursal.html'):
#     obj_del = Sucursal.objects.get(pk=id)
#     if request.method == 'POST':
#         obj_del.delete()
#         return redirect(reverse('sucursal'))
#     return render(request, template_name, {'object': obj_del})
