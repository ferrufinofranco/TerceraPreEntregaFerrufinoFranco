from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")
def cursos(request):
    allCursos = Curso.objects.all()
    context = {
        "cursos": allCursos
    }
    return render(request, "AppCoder/cursos.html", context=context)

def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)
def estudiantes(request):
    return render(request, "base.html")

def profesores(request):
    return render(request, "base.html")

def registroEstudiante(request):

    if request.method == 'POST':

        curso = Curso (request.POST['curso'], request.POST['camada'])

        curso.save()

        return render(request, "base.html")

    return render(request, "AppCoder/registroEstudiante.html")
