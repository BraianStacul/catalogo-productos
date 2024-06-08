from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django

from apps.usuarios.models import Usuario

def login(request):
    nombre_usuario = ""
    mensaje_error = None
    if request.method == "POST":
        nombre_usuario = request.POST.get("username")
        contrasenia = request.POST.get("password")
        u = authenticate(request, username=nombre_usuario, password=contrasenia)

        if u:
            login_django(request, u)

            return redirect("pagina_principal")
        else:
            mensaje_error = "Usuario y/o contraseña incorrecta"

    ctx = {
        "nombre_usuario": nombre_usuario,
        "mensaje_error": mensaje_error
    }
    return render(request, 'login.html', ctx)

def home(request):
    template_name = 'home.html'

    ctx = {

    }

    return render(request, template_name, ctx)