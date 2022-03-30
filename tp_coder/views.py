from django.shortcuts import render
from tp_coder.forms import *
from tp_coder.models import *


# Create your views here.
def inicio(request):
        return render(request, 'index.html')

def automov(request):
    return render (request, 'automo.html')

def motoc(request):
    return render (request, 'motos.html')

def vend_(request):
    return render (request, 'vended.html')

def busqueda(request):
    return render (request, 'busqued.html')


def form_automov(request):
    if request.method == 'POST':
        prueba1 = Form_autos(request.POST)
        if prueba1.is_valid:
            informacion = prueba1.cleaned_data

            auto_nuevo = Automoviles(informacion['marca'], informacion['modelo'], informacion['kms'], informacion['anio'],)
            auto_nuevo.save()
        else:
            auto_nuevo = Form_autos()
        return render (request, 'tp_coder/automoviles', {'formulario':'auto_nuevo'})