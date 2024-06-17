from django.shortcuts import render

# Create your views here.

from apps.utils.decorators import verificar_permisos
from apps.usuarios.models import Usuario

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .models import Usuario
from .forms import EditUser

@verificar_permisos()
def listar_usuarios(request):
    template_name = 'usuarios/listar_todos.html'
    lista_usuarios = Usuario.objects.all().order_by("id")

    ctx = {
        'usuarios': lista_usuarios,
    }
    
    return render(request, template_name, ctx)

#Perfil del Usuario
class PerfilUsuario(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user
    
#EditarPerfil

class EditarPerfil(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = EditUser
    template_name = 'usuarios/editar_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user 

    def get_success_url(self):
        return reverse_lazy('usuarios:perfil')