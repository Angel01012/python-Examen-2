from app import db
from sqlalchemy import Numeric

class Jugador(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    edad = db.Column(db.Integer)
    valormercado = db.Column(db.Numeric(10, 2))

class Equipo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(250))
    cantidadjugadores = db.Column(db.Numeric(10, 0))
    precioactual  = db.Column(db.Numeric(10, 2))
    liga = db.Column(db.String(250))

class Patrocinador(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(250))
    presupuesto = db.Column(db.Numeric(8, 4))
    añoscontratado = db.Column(db.Integer)
    pais = db.Column(db.String(250))

class Mercancia(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(250))
    tipomercancia = db.Column(db.String(250))
    precio = db.Column(db.Numeric(10, 2))
    edicion = db.Column(db.String(250))

class Partido(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    equipovisitante = db.Column(db.String(250))
    equipolocal = db.Column(db.String(250))
    arbitro = db.Column(db.String(250))
    balon = db.Column(db.String(250))
