from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import CursoForm, ProfesorForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")
def cursos(request):

    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            curso_save.save()


    allCursos = Curso.objects.all()
    context = {
        "cursos": allCursos,
        "form": CursoForm()
    }
    return render(request, "AppCoder/cursos.html", context=context)

def estudiantes(request):
    return render(request, "base.html")

def profesores(request):

    if request.method == 'POST':
        formProfesor = ProfesorForm(request.POST)

        if formProfesor.is_valid():
            informacion = formProfesor.cleaned_data
            profe_save = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profe_save.save()

    allProfesores = Profesor.objects.all()
    context = {
        "Profesores": allProfesores,
        "form": ProfesorForm()
    }
    return render(request, "AppCoder/registroProfesores.html", context=context)

def registroEstudiante(request):

    if request.method == 'POST':

        estudiante = Estudiante(request.POST['nombre'],
                                request.POST['apellido'],
                                request.POST['email'])
        estudiante.save()

        return render(request, "base.html")

    return render(request, "AppCoder/registroEstudiante.html")