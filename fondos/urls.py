from django.urls import path

from  fondos.views import *
app_name = 'fondos'
urlpatterns = [

    path('fondo/<int:pk>',publicacion_view.as_view(),name='index'),
    path('crear_publicacion', publicacion_create.as_view(), name='crear'),
    path('', tipo_view.as_view(), name='tipo'),
    path('publicacion/<int:pk>', publicacion_object.as_view(), name="ver"),
]