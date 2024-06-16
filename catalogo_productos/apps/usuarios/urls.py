from django.urls import path
from .views import PerfilUsuario, EditarPerfil

from . import views

app_name = "usuarios"

urlpatterns = [
    path('listar-todos/', views.listar_usuarios, name='listar_todos'),
    path('perfil/', PerfilUsuario.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfil.as_view(), name='editar_perfil'),
]