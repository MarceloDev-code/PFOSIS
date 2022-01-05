from django.shortcuts import render, get_list_or_404, get_object_or_404
from fondos.forms import *
from django.utils import timezone
from django.views.generic import TemplateView, ListView,CreateView
from fondos.models import *
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from django.contrib.auth import get_user_model


class publicacion_view(ListView):
    model = publicaciones
    template_name = 'index.html'
    paginate_by = 50
    def get_context_data(self,*args, **kwargs):
        ctx =super().get_context_data(*args,**kwargs)
        slug= self.kwargs['pk']
        ctx['publicaciones2'] = publicaciones.objects.filter(dimension=slug)
        return ctx

class publicacion_create(CreateView):
    model = publicaciones
    template_name = 'publicaciones/crear_publicacion.html'
    form_class = publicacionForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('fondos:tipo')



class tipo_view(ListView):
    model = dimensiones
    template_name = 'home.html'
    queryset = dimensiones.objects.all()

def lista_publicaciones(request,pk,*args,**kwargs):
    ctx = {}
    ctx['publicaciones1'] = publicaciones.objects.filter(dimension_id=pk).order_by('fecha_inicio')

    return render(request, 'index.html',ctx)


