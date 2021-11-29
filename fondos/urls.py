from django.urls import path

from  fondos.views import *
app_name = 'fondos'
urlpatterns = [

    path('',publicacion_view.as_view(),name='index'),
    path('crear_publicacion', publicacion_create.as_view(), name='crear'),

]