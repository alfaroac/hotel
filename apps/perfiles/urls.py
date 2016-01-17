from django.conf.urls import url
from .views import buscarPorDni

urlpatterns = [
  	url(r'^$', 'apps.perfiles.views.main', name='main'), 
	
	url(r'^huesped$','apps.perfiles.views.huesped', name='huesped'),
	url(r'^huesped/add$','apps.perfiles.views.addHuesped', name='addHuesped'),
	url(r'^huesped/upd/(?P<id>\d+)$','apps.perfiles.views.updHuesped', name='updHuesped'),
	url(r'^huesped/del/(?P<id>\d+)$', 'apps.perfiles.views.delHuesped', name='delHuesped'),

	url(r'^buscar/$', buscarPorDni.as_view(), name='buscarDni'),
	url(r'^personal$','apps.perfiles.views.listPersonal', name='personal'),
	

	url(r'^roles$','apps.perfiles.views.listRoles', name='roles'),
	url(r'^rol/add$','apps.perfiles.views.addRoles', name='addRoles'),
	url(r'^rol/upd/(?P<id>\d+)$','apps.perfiles.views.updRoles', name='updRoles'),
	#url(r'^buscar/$', buscarPorApellidos.as_view(), name='buscarApellidos'),
	#url(r'^huesped/busqueda/$', 'apps.perfiles.views.busqueda', name='busquedaHuesped'),
	#url(r'^guardarevento$', 'apps.agenda.views.guardarEvento'),
]