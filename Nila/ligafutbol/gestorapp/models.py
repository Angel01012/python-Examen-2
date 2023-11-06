from django.db import models

# Create your models here.
class Equipo(models.Model):
    cantidad_jugadores= models.IntegerField()
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"Cantidad de jugadores: {self.cantidad_jugadores}, Nombre: {self.nombre}"

class Liga(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"
    
class Patrocinador(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    numero_jugador = models.IntegerField()
    posicion = models.CharField(max_length=255)
    equipo = models.ForeignKey(Equipo,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Numero de jugador: {self.numero_jugador}, Posicion: {self.posicion}, Equipo: {self.equipo}"
 
class Partido(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    nombre_arbitro = models.CharField(max_length=255)
    goles = models.IntegerField()
    liga = models.ForeignKey(Liga,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"Nombre del equipo: {self.nombre_equipo}, Nombre del arbitro: {self.nombre_arbitro}, Goles: {self.goles}, Liga {self.liga}"