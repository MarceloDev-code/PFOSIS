from django.shortcuts import render, get_list_or_404, get_object_or_404
from fondos.forms import *
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from fondos.models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

class publicacion_view(ListView):
    model = publicaciones
    template_name = 'index.html'
    paginate_by = 50




