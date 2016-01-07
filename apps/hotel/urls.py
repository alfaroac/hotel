from django.conf.urls import url

urlpatterns = [
  	   	
   	url(r'^habitacion$','apps.hotel.views.habitacion', name='habitacion'),
   	url(r'^habitacion/add$','apps.hotel.views.addHabitacion', name='addHabitacion'),
   	url(r'^habitacion/upd/(?P<id>\d+)$','apps.hotel.views.updHabitacion', name='updHabitacion'),
   	url(r'^habitacion/del/(?P<id>\d+)$', 'apps.hotel.views.delHabitacion', name='delHabitacion'),
]