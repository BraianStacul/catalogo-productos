from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django

def home(request):
    template_name = 'home.html'

    ctx = {

    }

    return render(request, template_name, ctx)