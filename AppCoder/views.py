from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.
def guardar_curso(request,camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("curso creado existosamente")
