from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView

from .models import Producto

class Listar(ListView):
    template_name='productos/listar.html'
    model = Producto
    context_object_name = 'productos'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("nombre")