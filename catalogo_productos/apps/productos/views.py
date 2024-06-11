# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import ProductoForm, CForm, VerForm
from .models import Producto, Categoria

class Listar(ListView):
    template_name='productos/listar.html'
    model = Producto
    context_object_name = 'productos'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().filter(activo = True).order_by("nombre")

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

class Editar(UpdateView):
    template_name = "productos/editar.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("productos:listar")

class EditarCategoria(UpdateView):
    template_name = "productos/editar_categoria.html"
    model = Categoria
    form_class = CForm
    success_url = reverse_lazy("productos:listar_categorias")

class Eliminar(DeleteView):
    model = Producto
    success_url = reverse_lazy("productos:listar")

class EliminarCategoria(DeleteView):
    model = Categoria
    success_url = reverse_lazy("productos:listar_categorias")

class ViewProducto(UpdateView):
    template_name = "productos/ver_detalle.html"
    model = Producto
    form_class = VerForm
    success_url = reverse_lazy("productos:listar")

class Desactivar(DeleteView):
    model = Producto

    def post(self, request,pk, *args, **kwargs):
        object = Producto.objects.get(id = pk)
        object.activo = False
        object.save()
        return redirect("productos:listar")