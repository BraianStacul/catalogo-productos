# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ProductoForm
from .models import Producto

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