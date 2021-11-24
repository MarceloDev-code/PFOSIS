from django.urls import path

from  fondos.views import *
app_name = 'fondos'
urlpatterns = [

    path('',publicacion_view.as_view(),name='index'),



]