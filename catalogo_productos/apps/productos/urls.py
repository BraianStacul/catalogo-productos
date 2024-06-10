from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path('listar/', views.Listar.as_view(), name='listar'),
    path('listar-categorias/', views.ListarCategorias.as_view(), name='listar_categorias'),
    path('nuevo/', views.Nuevo.as_view(), name='nuevo'),
    path('nueva-categoria/', views.NuevaCategoria.as_view(), name='nueva_categoria')
]