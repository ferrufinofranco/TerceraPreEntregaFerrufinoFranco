from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('home/', home, name="Home"),
    path('cursos/', cursos, name="AppCoderCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name='AppCoderCurso'),
    path('estudiantes/', estudiantes, name="AppCoderEstudiantes"),
    path('profesores/', profesores, name='AppCoderProfesores'),
    path('registroEstudiante/', views.registroEstudiante, name='registroEstudiante')
]
