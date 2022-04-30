from django.shortcuts import render

from blogapp.models import Usuario

# Create your views here.

def index(request):
    return render(request,"blogapp/index.html")

def usuarios(request):
    usuario=Usuario.objects.all()
    return render (request, 'blogapp/usuarios.html', {"data":usuario})