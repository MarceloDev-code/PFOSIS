from django.shortcuts import render, get_list_or_404, get_object_or_404
from fondos.forms import *
from django.utils import timezone
from django.views.generic import TemplateView, ListView,CreateView
from fondos.models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

class publicacion_view(ListView):
    model = publicaciones
    template_name = 'index.html'
    paginate_by = 50
    queryset = publicaciones.objects.filter(activo=True).order_by('fecha_inicio')
class publicacion_create(CreateView):
    model = publicaciones
    template_name = 'publicaciones/crear_publicacion.html'
    form_class = publicacionForm


