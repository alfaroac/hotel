from django.conf.urls import url

urlpatterns = [
  	   	
   	url(r'^habitacion$','apps.hotel.views.habitacion', name='habitacion'),
   	url(r'^habitacion/add$','apps.hotel.views.addHabitacion', name='addHabitacion'),
   	url(r'^habitacion/upd/(?P<id>[0-9]+)$','apps.hotel.views.updHabitacion', name='updHabitacion'),
   	url(r'^habitacion/del/(?P<id>\d+)$', 'apps.hotel.views.delHabitacion', name='delHabitacion'),

   	url(r'^registro$','apps.hotel.views.registro', name='registro'),
   	url(r'^registro/add$','apps.hotel.views.addRegistro', name='addRegistro'),
   	url(r'^registro/upd/(?P<id>\d+)$','apps.hotel.views.updRegistro', name='updRegistro'),
   	url(r'^registro/del/(?P<id>\d+)$', 'apps.hotel.views.delRegistro', name='delRegistro'),

	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]