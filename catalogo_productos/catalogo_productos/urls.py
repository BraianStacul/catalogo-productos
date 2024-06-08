from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='pagina_principal'),

    # Login & Logout
    path('login/', views.login, name="iniciar_sesion"),
    
    # Includes
    path("usuarios/", include('apps.usuarios.urls'))
]
