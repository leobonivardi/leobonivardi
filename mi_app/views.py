from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiante, Familia, Profesor
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario, ProfesorFormulario, FamiliaFormulario, ProfesorBusquedaFormulario


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")


def saludo_personalizado(request):
    pass

def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo": "Hola este es mi primer website!!!"})

def listar_cursos(request): # vista
    context = {}
    context["cursosssssss"] = Curso.objects.all() # modelo
    return render(request, "mi_app/lista_cursos.html", context) # template


def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)

def listar_familiares(request):
    context= {}
    context["familiares"] = Familia.objects.all()
    return render(request,"mi_app/lista_familiares.html", context)
    

def formulario_curso(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre= datos["nombre"], camada= datos["camada"])
            curso.save()
            
            return  render(request, "mi_app/curso_formulario.html", {"mensaje":"agregado con exito!"})
        
        
    else:
        mi_formulario = CursoFormulario()
    return render(request,"mi_app/curso_formulario.html",{"mi_formulario":mi_formulario})
        

def formulario_busqueda(request):
    
    busqueda_formulario = CursoBusquedaFormulario()
    
    if request.GET:    
        busqueda_formulario = CursoBusquedaFormulario(request.GET)
        if busqueda_formulario.is_valid():
            cursos = Curso.objects.filter(curso=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "mi_app/busqueda_curso.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})
    
    return render(request, "mi_app/busqueda_curso.html",{"busqueda_formulario": busqueda_formulario})



def formulario_profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
           
        if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                email=informacion['email'], profesion=informacion['profesion']) 

                profesor.save()

                return render(request, "mi_app/formulario_profesores.html")

    else: 
            miFormulario= ProfesorFormulario()
    return render(request, "mi_app/formulario_profesores.html", {"miFormulario":miFormulario})
  
  
  
def formulario_familiar(request):
    if request.method == "POST":
        mi_formulario3 = FamiliaFormulario(request.POST)
        print(mi_formulario3)
        
        if mi_formulario3.is_valid:
            info = mi_formulario3.cleaned_data
            familia = Familia(nombre= info["nombre"], edad= info["edad"])
            familia.save()
            
            return  render(request, "mi_app/formulario_familiar.html", {"mensaje":"agregado con exito!"})
        
        
    else:
        mi_formulario3 = FamiliaFormulario()
    return render(request,"mi_app/formulario_familiar.html",{"mi_formulario":mi_formulario3})


def formulario_busqueda2(request):
    
    busqueda_formulario2 = ProfesorBusquedaFormulario()
    
    if request.GET:    
        busqueda_formulario2 = ProfesorBusquedaFormulario(request.GET)
        if busqueda_formulario2.is_valid():
            profesores = Curso.objects.filter(nombre=busqueda_formulario2.cleaned_data.get("criterio")).all()
            return render(request, "mi_app/busqueda_profesor.html", {"busqueda_formulario": busqueda_formulario2, "profesores": profesores})
    
    return render(request, "mi_app/busqueda_profesor.html",{"busqueda_formulario": busqueda_formulario2})