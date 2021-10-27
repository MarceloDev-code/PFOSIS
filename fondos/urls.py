from django.urls import path

from  fondos.views import *
app_name = 'fondos'
urlpatterns = [

    path('',index,name='index'),


]