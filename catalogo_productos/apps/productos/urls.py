from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path('listar/', views.Listar.as_view(), name='listar'),
    path('listar-categorias/', views.ListarCategorias.as_view(), name='listar_categorias'),
    path('nuevo/', views.Nuevo.as_view(), name='nuevo'),
    path('nueva-categoria/', views.NuevaCategoria.as_view(), name='nueva_categoria'),
    path('editar/<int:pk>/', views.Editar.as_view(), name='editar'),
    path('editar-categoria/<int:pk>/', views.EditarCategoria.as_view(), name='editar_categoria'),
    path('eliminar/<int:pk>/', views.Eliminar.as_view(), name='eliminar'),
    path('eliminar-categoria/<int:pk>/', views.EliminarCategoria.as_view(), name='eliminar_categoria'),
    path('detalle-producto/<int:pk>/,', views.ViewProducto.as_view(), name='ver_detalle')
]