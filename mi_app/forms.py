from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=40)

class ProfesorBusquedaFormulario(forms.Form):
    criterio = forms.CharField()



class FamiliaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    
    
