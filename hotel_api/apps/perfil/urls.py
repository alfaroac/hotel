from django.conf.urls import url
from .views import *

urlpatterns = [

	url(r'^tipo$', list_tipo , name='tipo'),
    url(r'^tipo/add/$', creartipo, name='add_tipo'),
    url(r'^tipodel/$', tipo_del),

    url(r'^detalle_perfil$', perfil_detail, name= 'detail_perfil'),
    url(r'^edit_perfil$', perfil_edit, name= 'edit_perfil'),

    url(r'^users$', UserList.as_view(), name='user_list'),
    url(r'^user_add$', UserCreate.as_view(), name='user_add'),
    url(r'^user_del/(?P<pk>\d+)$', UserDelete.as_view(), name='user_del'),
    url(r'^user_edit$', user_edit, name= 'user_edit'),

    url(r'^registrar$', RegistrarUsuario.as_view(), name='registrar_usuario'),

    # url(r'^upload', upload, name = 'upload')
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT, }),
]
