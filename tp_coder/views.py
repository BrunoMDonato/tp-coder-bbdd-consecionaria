from django.shortcuts import render
from tp_coder.forms import *
from tp_coder.models import *


# Create your views here.
def inicio(request):
        return render(request, 'index.html')

def automov(request):

    autito = Automoviles.objects.all()

    if request.method == 'POST':
        formulario =  Form_autos(request.POST)
   
        if formulario.is_valid():
            datos = formulario.cleaned_data

            autito = Automoviles(marca = datos['marca'], modelo=datos['modelo'],kms=datos['kms'], anio=datos['anio'], chasis=datos['chasis'])
            autito.save()
        

        formulario = Form_autos()
        return render(request, 'tp_coder/automo.html', {'Autos': autito, 'modelo':'Automoviles', 'marca': 'Automoviles', 'formulario': formulario})

    elif request.method == 'GET':
        formulario = Form_autos
        return render(request, 'tp_coder/automo.html', {'Autos': autito, 'modelo':'Automoviles', 'marca': 'Automoviles', 'formulario': formulario})


def motoc(request):

    motito = Motocicletas.objects.all()

    if request.method == 'POST':
        formulario =  Form_motos(request.POST)
        print(formulario)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            motito = Motocicletas(marca=datos['marca'], modelo=datos['modelo'],kms=datos['kms'], anio=datos['anio'], chasis=datos['chasis'])
            motito.save()

        formulario = Form_motos()
        return render (request, 'tp_coder/motos.html', {'Motos': motito, 'modelo':'Motocicletas', 'marca': 'Motocicletas', 'kms': 'Motocicleta', 'anio':'Motocicletas','chasis':'Motocicletas',  'formulario': formulario})

    elif request.method == 'GET':
        formulario = Form_motos()
        return render(request, 'tp_coder/motos.html')



def vend_(request):
    
    vendedorcito = Vendedor.objects.all()

    if request.method == 'POST':
        formulario =  Forms_vend(request.POST)
     
        if formulario.is_valid():
            datos = formulario.cleaned_data

            vendedorcito = Vendedor(datos['id_vend'], datos['nombre'])
            vendedorcito.save()

            formulario = Forms_vend()
            return render (request, 'tp_coder/vended.html', {'Vendedor': vendedorcito, 'id_vend':'Vendedor', 'nombre': 'Vendedor', 'formulario': formulario})

    elif request.method == 'GET':
        formulario = Forms_vend
        return render (request, 'tp_coder/vended.html')

def busqueda(request):
    return render (request, 'busqued.html')


