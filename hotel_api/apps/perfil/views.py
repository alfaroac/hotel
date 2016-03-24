# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from .forms import *
from .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, FormView
from django.contrib.auth.models import User

# Create your views here.
class TipoUsuarioView(ListView):

    template_name = "perfil/tipo/list_tipo.html"
    model = TipoUsuario
    context_object_name = 'listas'


class CreateTipoUsuario(CreateView):
    form_class = TipoUsuarioForm
    template_name = "perfil/tipo/add_tipo.html"
    success_url = reverse_lazy('perfiles_app:tipo')

    def form_valid(self, form):
        return super(CreateTipoUsuario, self).form_valid(form)


class EditTipoUsuario(UpdateView):
    form_class = TipoUsuarioForm
    template_name = "perfil/tipo/upd_tipo.html"
    model = TipoUsuario
    success_url = reverse_lazy('perfiles_app:tipo')


class DeleteTipoUsuario(DeleteView):
    template_name = "perfil/tipo/del_tipo.html"
    model = TipoUsuario
    success_url = reverse_lazy('perfiles_app:tipo')
    context_object_name = 'object'


class PerfilList(ListView):
    template_name = "perfil/list_perfil.html"
    model = Perfil


class PerfilCreate(CreateView):
    template_name = "perfil/add_perfil.html"
    form_class = PerfilForm
    success_url = reverse_lazy('index')


class PerfilEdit(UpdateView):
    form_class = PerfilForm
    template_name = "perfil/upd_perfil.html"
    model = Perfil
    success_url = reverse_lazy('perfiles_app:list_perfil')


class PerfilDelete(DeleteView):
    template_name = "perfil/del_perfil.html"
    model = Perfil
    success_url = reverse_lazy('perfiles_app:list_perfil')
    context_object_name = 'object'


class PerfilDetail(DetailView):
    template_name = "perfil/det_perfil.html"
    model = Perfil


def perfil_detail(request):
    user = request.user
    perfil = Perfil.objects.get(usuario=user)
    ctx = {'perfil': perfil}
    return render(request, 'perfil/det_perfil.html', ctx)



def perfil_edit(request):
    template = 'perfil/upd_perfil.html'
    user = request.user
    perfil = Perfil.objects.get(usuario=user)
    idp = perfil.id
    obj = Perfil.objects.get(pk=idp)
    if request.method == 'POST':
        modelform = PerfilForm(request.POST, request.FILES,
                               instance=obj)
        if modelform.is_valid():
            modelform.save()
            return redirect(reverse('index'))
    else:
        modelform = PerfilForm(instance=obj)
        ctx = {'form': modelform}
        context_instance = RequestContext(request)
    return render(request, template, ctx, context_instance)

class RegistrarUsuario(FormView):
    template_name = 'users/registrar_usuario.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('perfiles_app:list_perfil')
    def form_valid(self, form):
        user = form.save()
        perfil = Perfil()
        perfil.usuario = user
        perfil.rol = form.cleaned_data['rol']
        perfil.dni = form.cleaned_data['dni']
        perfil.sexo = form.cleaned_data['sexo']
        perfil.telefono = form.cleaned_data['telefono']
        perfil.codigo = form.cleaned_data['codigo']
        perfil.direccion = form.cleaned_data['direccion']
        perfil.celular = form.cleaned_data['celular']
        perfil.estado = form.cleaned_data['estado']
        perfil.imagen = form.cleaned_data['imagen']
        perfil.save()
        return super(RegistrarUsuario, self).form_valid(form)

class UserList(ListView):
    template_name = 'users/user_list.html'
    model = User

class UserCreate(CreateView):
    template_name = 'users/user_add.html'
    form_class = UserForm
    success_url = reverse_lazy('perfiles_app:user_list')
    def form_valid(self, form):
        user = form.save()
        perfil = Perfil()
        perfil.usuario = user
        perfil.codigo = form.cleaned_data['codigo']
        perfil.save()
        return super(UserCreate, self).form_valid(form)

class UserDelete(DeleteView):
    template_name = "users/user_del.html"
    model = User
    success_url = reverse_lazy('perfiles_app:user_list')
    # context_object_name = 'object'

def user_edit(request):
    template = 'users/upd_user.html'
    user = request.user
    up = User.objects.get(username=user)
    idp = up.id
    obj = User.objects.get(pk=idp)
    if request.method == 'POST':
        modelform = UserForm(request.POST, request.FILES,
                               instance=obj)
        if modelform.is_valid():
            modelform.save()
            return redirect(reverse('index'))
    else:
        modelform = UserForm(instance=obj)
        # ctx = {'form': modelform}
        # context_instance = RequestContext(request)
    return render(request, template,{'form': modelform} , context_instance = RequestContext(request))
