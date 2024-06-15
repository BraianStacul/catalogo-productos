from django.shortcuts import render

# Create your views here.

from apps.utils.decorators import verificar_permisos
from apps.usuarios.models import Usuario

@verificar_permisos()
def listar_usuarios(request):
    template_name = 'usuarios/listar_todos.html'
    lista_usuarios = Usuario.objects.all().order_by("id")

    ctx = {
        'usuarios': lista_usuarios,
    }
    
    return render(request, template_name, ctx)