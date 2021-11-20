from django.shortcuts import render, get_list_or_404, get_object_or_404
from fondos.forms import *
from django.utils import timezone
from django.views.generic import TemplateView
from fondos.models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def index(request,*args,**kwargs):
    ctx = {}
    lista = publicaciones.objects.filter(activo=True).order_by('fecha_termino')
    ctx['publicaciones'] = lista
    publicaciones.cambio_de_estado(publicaciones)
    return render(request,'index.html',ctx)




