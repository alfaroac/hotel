from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.views import logout_then_login, login
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^home/$', Homepage.as_view(), name='homepage'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^hotel/', include('apps.hotel.urls', namespace='hotel_app')),
    url(r'^perfil/', include('apps.perfil.urls', namespace='perfil_app')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT, }),
]
