from django.conf.urls import url
from .views import *

urlpatterns = [

	# url(r'^tipo$',TipoUsuarioView.as_view(), name='tipo'),
    # url(r'^tipo/nuevo$', CreateTipoUsuario.as_view(),
        # name='add_tipo'),
    # url(r'^tipo/editar/(?P<pk>\d+)$',
        # EditTipoUsuario.as_view(), name='upd_tipo'),
    # url(r'^tipo/eliminar/(?P<pk>\d+)$',
        # DeleteTipoUsuario.as_view(), name='del_tipo'),
]
