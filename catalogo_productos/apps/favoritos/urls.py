from django.urls import path

from . import views

app_name= "favoritos"

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('quitar/<int:producto_id>/', views.quitar_favorito, name='quitar_favorito'),
    path('listar/', views.Listar.as_view(), name='listar'),
    path('quitar_detalle/<int:producto_id>/', views.quitar_favorito_detalle, name='quitar_favorito_detalle'),
]