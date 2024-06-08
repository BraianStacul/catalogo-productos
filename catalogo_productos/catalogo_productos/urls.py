from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='pagina_principal'),

    # Login & Logout

    # Includes
    path("usuarios/", include('apps.usuarios.url'))
]
