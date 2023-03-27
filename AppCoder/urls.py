from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('home/', home, name="Home"),
    path('registroCursos/', registroCursos, name="AppCoderCursos"),
    path('busquedaCursos/', busquedaCursos, name="AppCoderBusquedaCursos"),
    path('registroProfesores/', registroProfesores, name='AppCoderRegistroProfesores'),
    path('registroEstudiante/', registroEstudiante, name='AppCoderRegistroEstudiante')
]
