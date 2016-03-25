from django.conf.urls import url
from .views import *

urlpatterns = [

	url(r'^tipo$',TipoUsuarioView.as_view(), name='tipo'),
    url(r'^tipo/nuevo$', CreateTipoUsuario.as_view(),
        name='add_tipo'),
    url(r'^tipo/editar/(?P<pk>\d+)$',
        EditTipoUsuario.as_view(), name='upd_tipo'),
    url(r'^tipo/eliminar/(?P<pk>\d+)$',
        DeleteTipoUsuario.as_view(), name='del_tipo'),

    url(r'^lista$', PerfilList.as_view(), name='list_perfil'),
    url(r'^nuevo$', PerfilCreate.as_view(), name='add_perfil'),
    url(r'^editar/(?P<pk>\d+)$', PerfilEdit.as_view(), name='upd_perfil'),
    url(r'^detalle/(?P<pk>\d+)$', PerfilDetail.as_view(), name='det_perfil'),
    url(r'^eliminar/(?P<pk>\d+)$', PerfilDelete.as_view(), name='del_perfil'),

    url(r'^detalle_perfil$', perfil_detail, name= 'detail_perfil'),
    url(r'^edit_perfil$', perfil_edit, name= 'edit_perfil'),

    url(r'^users$', UserList.as_view(), name='user_list'),
    url(r'^user_add$', UserCreate.as_view(), name='user_add'),
    url(r'^user_del/(?P<pk>\d+)$', UserDelete.as_view(), name='user_del'),
    url(r'^user_edit$', user_edit, name= 'user_edit'),

    url(r'^registrar$', RegistrarUsuario.as_view(), name='registrar_usuario'),

    url(r'^tipo/add/$', creartipo),
    url(r'^tipo/crear/$',CreateTipoUsuario.as_view()),
    # url(r'^upload', upload, name = 'upload')
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT, }),
]
