from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from apps.utils.decorators import verificar_favorito

from .models import Favorito

# Create your views here.

class Listar(LoginRequiredMixin, ListView):
    template_name='favoritos/listar.html'
    model = Favorito
    context_object_name = 'favoritos'
    paginate_by = 20

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

@verificar_favorito()
def agregar_favorito(request, producto_id):
    if request.method == 'POST':
        # Verificar si el producto ya está en la lista de favoritos
        if Favorito.objects.filter(usuario=request.user, producto_id=producto_id).exists():
            messages.warning(request, 'Este producto ya está en tu lista de favoritos.')
        else:
            Favorito.objects.create(usuario=request.user, producto_id=producto_id)
            messages.success(request, 'Producto agregado a favoritos exitosamente.')

    return redirect('productos:listar')

@verificar_favorito()
def quitar_favorito(request, producto_id):
    if request.method == 'POST':
        # Verificar si el producto está en la lista de favoritos del usuario
        if Favorito.objects.filter(usuario=request.user, producto_id=producto_id).exists():
            Favorito.objects.filter(usuario=request.user, producto_id=producto_id).delete()
            messages.success(request, 'Producto eliminado de favoritos exitosamente.')
        else:
            messages.error(request, 'El producto no está en la lista de favoritos.')
    return redirect('productos:listar')

@verificar_favorito()
def quitar_favorito_detalle(request, producto_id):
    if request.method == 'POST':
        if Favorito.objects.filter(usuario=request.user, producto_id=producto_id).exists():
            Favorito.objects.filter(usuario=request.user, producto_id=producto_id).delete()
            messages.success(request, 'Producto eliminado de favoritos exitosamente.')
    return redirect('favoritos:listar')

