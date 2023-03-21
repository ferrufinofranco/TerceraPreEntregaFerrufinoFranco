from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('home/', home, name="Home"),
    path('cursos/', cursos, name="AppCoderCursos"),
    path('estudiantes/', estudiantes, name="AppCoderEstudiantes"),
    path('registroProfesores/', profesores, name='AppCoderRegistroProfesores'),
    path('registroEstudiante/', registroEstudiante, name='AppCoderRegistroEstudiante')
]
