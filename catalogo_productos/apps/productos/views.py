# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ProductoForm, CForm
from .models import Producto, Categoria

class Listar(ListView):
    template_name='productos/listar.html'
    model = Producto
    context_object_name = 'productos'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("nombre")

class Nuevo(LoginRequiredMixin,CreateView):
    template_name = "productos/crear.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("productos:listar")

class ListarCategorias(ListView):
    template_name='productos/listar_categorias.html'
    model = Categoria
    context_object_name = 'categorias'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("id")
    
class NuevaCategoria(CreateView):
    template_name = "productos/crear_categoria.html"
    model = Categoria
    form_class = CForm
    success_url = reverse_lazy("productos:listar_categorias")