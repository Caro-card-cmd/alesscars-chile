from django.urls import path
from . import views   #se importan las vistas de la app
from django.conf import settings   #se importa la configuracion del settings
from django.contrib.staticfiles.urls import static  #se importa el static de settings


urlpatterns = [ 
    path('',views.index,name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('servicios', views.servicios, name='servicios'),
    path('gracias', views.gracias, name='gracias'),
    path('logear/', views.logear, name='logear'),
    path('registro/', views.registro, name='registro'),
    path('exit/',views.exit,name='exit'),
    path('gestion/',views.gestion,name='gestion'),
    path('servicio/crear/',views.crear_servicio,name='crear_servicio'),
    path('servicio/eliminar/<int:id>',views.eliminar,name='eliminar_servicio'),   # path('servicio/eliminar/: se fija la url, <int:id>': parametro dinamico, es el id del servidor que se elimina
    path('servicio/editar/<int:id>',views.editar_servicio,name='editar_servicio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #sirve para que Django pueda mostrar los archivos multimendia, 
                                                                    #settings.MEDIA_URL: se accede a los archivos
                                                                    #document_root=settings.MEDIA_ROOT: carpeta fisica donde se guardan los archivos