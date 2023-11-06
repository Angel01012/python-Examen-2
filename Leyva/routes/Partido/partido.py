from flask import Blueprint,request,redirect,render_template,url_for,jsonify
from models import Partido
from app import db

apppartido = Blueprint('apppartido',__name__,template_folder="templates")

@apppartido.route('/ConsultarPartidos',methods=["GET"])
def consultartodos():
    json = request.get_json()
    partidos = Partido.query.all()
    cad = ""
    for partido in partidos:
        cad = cad + f"id: {partido.id}, EV: {partido.equipovisitante}, EL: {partido.equipolocal}, arbitro: {partido.arbitro}, balon: {partido.balon}\n" 

    respuesta =  jsonify(cad)
    return respuesta

@apppartido.route('/ConsultarPartido',methods=["GET"])
def consultaruno():
    json = request.get_json()
    partido = Partido.query.get_or_404(json["id"])
    cad = cad + f"id: {partido.id}, EV: {partido.equipovisitante}, EL: {partido.equipolocal}, arbitro: {partido.arbitro}, balon: {partido.balon}\n" 
    respuesta = jsonify(cad)
    return respuesta

@apppartido.route('/AgregarPartido',methods=["POST"])
def agregarpartido():
    json = request.get_json()
    partido = Partido()
    partido.equipovisitante = json["equipovisitante"]
    partido.equipolocal = json["equipolocal"]
    partido.arbitro = json["arbitro"]
    partido.balon = json["balon"]
    db.session.add(partido)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"partido agregado"})
    return respuesta

@apppartido.route('/EditarPartido',methods = ["PUT"])
def editarpartido():
    json = request.get_json()
    partido = Partido.query.get_or_404(json["id"])
    partido.equipovisitante = json["equipovisitante"]
    partido.equipolocal = json["equipolocal"]
    partido.arbitro = json["arbitro"]
    partido.balon = json["balon"]
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"partido editado"})
    return respuesta

@apppartido.route('/BorrarPartido',methods=["DELETE"])
def borrarpartido():
    partido = Partido.query.get_or_404(request.headers['id'])
    db.session.delete(partido)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"partido eliminado"})
    return respuesta