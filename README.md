# TerceraPreEntregaFerrufinoFranco

Rutas de acceso:

http://127.0.0.1:8000/coder/home/ 
http://127.0.0.1:8000/coder/registroProfesores/ 
http://127.0.0.1:8000/coder/registroCursos/
http://127.0.0.1:8000/coder/busquedaCursos/ 
http://127.0.0.1:8000/coder/registroEstudiante/

El proyecto esta hecho sobre un template extraido de https://getbootstrap.com/

En el mismo puedes visualizar dentro del navbar distintas opciones que te redigiran al "Inicio", registros de cursos, profesores y estudiante. Y busqueda de cursos filtrando por nombre del curso.

Dentro de http://127.0.0.1:8000/coder/registroProfesores/ se registran profesores dentro de la base de datos, muestra un mensaje de registro exitoso. Hecho con API Django.

Dentro de http://127.0.0.1:8000/coder/registroCursos/ se registran cursos dentro de la base de datos. Hecho con API Django. Ya se encuentran registradas dos cursos

Dentro de http://127.0.0.1:8000/coder/registroEstudiante/ se registran estudiantes dentro de la base de datos. Hecho sin API Django, redirige a un HTML donde se visualiza el formulario.

Dentro de http://127.0.0.1:8000/coder/busquedaCursos/ se realiza la busqueda por nombre de cursos. La misma devuelve un listado de cursos que coincidan con la busqueda y las comisiones. Se puede probar con "Python"

