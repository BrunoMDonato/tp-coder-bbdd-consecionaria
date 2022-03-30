from urllib.parse import urlparse
from django.urls import path
from tp_coder.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('automoviles/', form_automov, name='Automoviles'),
    path('motocicletas/', motoc, name='Motos'),
    path('vendedores/', vend_, name='Vendedores'),
    path('busqueda/', busqueda, name='Buscar'),

]
