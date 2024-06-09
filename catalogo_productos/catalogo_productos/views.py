from django.shortcuts import render

from apps.usuarios.forms import FormularioRegistroUsuario

def home(request):
    template_name = 'home.html'

    ctx = {

    }

    return render(request, template_name, ctx)

def registrarme(request):
    template_name = "registrarme.html"
    form = FormularioRegistroUsuario()

    mensaje_todo_bien = None

    if request.method == "POST":
        form = FormularioRegistroUsuario(request.POST)

        if form.is_valid():
            mensaje_todo_bien = "Usuario creado correctamente, puede iniciar sesion"
            form.save()
        else:
            print("ERRORES: ", form.errors)

    ctx = {
        'form': form,
        "mensaje_todo_bien":mensaje_todo_bien
    }
    return render(request, template_name, ctx)