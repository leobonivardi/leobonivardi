from unittest.util import _MAX_LENGTH
from django.db import models


class Curso(models.Model):

    curso = models.CharField(max_length=40)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    


class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30) 
    
