from django.contrib import admin
from django.urls import path
from mi_app.views import (saludar_a, saludo, 
        saludo_personalizado, listar_cursos, listar_estudiantes,
        mostrar_index, listar_familiares,formulario_curso,
        formulario_busqueda, formulario_profesores,formulario_familiar,formulario_busqueda2)


urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludo-personalizado/', saludo_personalizado),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('listar-familiares/', listar_familiares),
    path('formulario-curso/', formulario_curso),
    path('buscar-curso/',  formulario_busqueda),
    path('formulario-profesores/', formulario_profesores),
    path('formulario-familiar/', formulario_familiar),
    path('buscar-profesor/', formulario_busqueda2)
]