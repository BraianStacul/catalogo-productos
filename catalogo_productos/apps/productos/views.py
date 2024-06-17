# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from apps.utils.mixins import VerificarAdmin

from .filterset import ProductoFilter

from .forms import ProductoForm, CForm, VerForm
from .models import Producto, Categoria
from apps.favoritos.models import Favorito

class Listar(FilterView):
    template_name='productos/listar.html'
    model = Producto
    context_object_name = 'productos'
    paginate_by = 20
    filterset_class=ProductoFilter

    def get_queryset(self):
        return self.model.objects.all().filter(activo = True).order_by("nombre")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = context['productos']

        # Creamos un lista para almacenar todos los favoritos del usuarios
        fpk = []

        if not self.request.user.is_anonymous:
            # Recorremos los favoritos del usuario actual y lo agregamos a la lista
            for f in Favorito.objects.filter(usuario=self.request.user, producto__in=productos):
                fpk.append(f.producto_id)

        context['Favoritos'] = fpk
        
        return context

class Nuevo(LoginRequiredMixin, VerificarAdmin, CreateView):
    template_name = "productos/crear.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("productos:listar")


class ListarCategorias(LoginRequiredMixin, VerificarAdmin, ListView, ):
    template_name='productos/listar_categorias.html'
    model = Categoria
    context_object_name = 'categorias'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("id")
    
class NuevaCategoria(LoginRequiredMixin, VerificarAdmin, CreateView):
    template_name = "productos/crear_categoria.html"
    model = Categoria
    form_class = CForm
    success_url = reverse_lazy("productos:listar_categorias")

class Editar(LoginRequiredMixin, VerificarAdmin, UpdateView):
    template_name = "productos/editar.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("productos:listar")

class EditarCategoria(LoginRequiredMixin, VerificarAdmin, UpdateView):
    template_name = "productos/editar_categoria.html"
    model = Categoria
    form_class = CForm
    success_url = reverse_lazy("productos:listar_categorias")

class Eliminar(LoginRequiredMixin, VerificarAdmin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos:listar")

class EliminarCategoria(LoginRequiredMixin, VerificarAdmin, DeleteView):
    model = Categoria
    success_url = reverse_lazy("productos:listar_categorias")

class ViewProducto(UpdateView):
    template_name = "productos/ver_detalle.html"
    model = Producto
    form_class = VerForm
    success_url = reverse_lazy("productos:listar")

class Desactivar(LoginRequiredMixin, VerificarAdmin, DeleteView):
    model = Producto

    def post(self, request,pk, *args, **kwargs):
        object = Producto.objects.get(id = pk)
        object.activo = False
        object.save()
        return redirect("productos:listar")