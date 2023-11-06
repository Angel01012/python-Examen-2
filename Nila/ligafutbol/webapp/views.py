from django.shortcuts import render
from gestorapp.models import Equipo,Liga,Patrocinador,Jugador,Partido

# Create your views here.
def index(request):
    return render(request, 'indexLiga.html')


def indexGestorapp(request):
    equipos = Equipo.objects.order_by('id')
    ligas  = Liga.objects.order_by('id')
    patrocinadores = Patrocinador.objects.order_by('id')
    jugadores = Jugador.objects.order_by('id')
    partidos  = Partido.objects.order_by('id')
    return render(request,'indexLiga.html', {"ligas":ligas})
