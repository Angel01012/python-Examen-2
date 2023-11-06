from flask import Blueprint,request,redirect,render_template,url_for,jsonify
from models import Jugador
from app import db

appjugador = Blueprint('appjugador',__name__,template_folder="templates")

@appjugador.route('/ConsultarJugadores',methods=["GET"])
def consultartodos():
    json = request.get_json()
    jugadores = Jugador.query.all()
    cad = ""
    for jugador in jugadores:
        cad = cad + f"id: {jugador.id}, nombre: {jugador.nombre}, apellido: {jugador.apellido}, edad: {jugador.edad}, valormercado: {jugador.valormercado}\n" 

    respuesta =  jsonify(cad)
    return respuesta

@appjugador.route('/ConsultarJugador',methods=["GET"])
def consultaruno():
    json = request.get_json()
    jugador = Jugador.query.get_or_404(json["id"])
    cad = f"id: {jugador.id}, nombre: {jugador.nombre}, apellido: {jugador.apellido}, edad: {jugador.edad}, valormercado: {jugador.valormercado}\n"
    respuesta = jsonify(cad)
    return respuesta

@appjugador.route('/AgregarJugador',methods=["POST"])
def agregarjugador():
    json = request.get_json()
    jugador = Jugador()
    jugador.nombre = json["nombre"]
    jugador.edad = json["edad"]
    jugador.apellido = json["apellido"]
    jugador.valormercado = json["valormercado"]
    db.session.add(jugador)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"jugador agregado"})
    return respuesta

@appjugador.route('/EditarJugador',methods = ["PUT"])
def editarjugador():
    json = request.get_json()
    jugador = Jugador.query.get_or_404(json["id"])
    jugador.nombre = json["nombre"]
    jugador.edad = json["edad"]
    jugador.apellido = json["apellido"]
    jugador.valormercado = json["valormercado"]
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"jugador editado"})
    return respuesta

@appjugador.route('/BorrarJugador',methods=["DELETE"])
def borrarjugador():
    jugador = Jugador.query.get_or_404(request.headers['id'])
    db.session.delete(jugador)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"jugador eliminado"})
    return respuesta